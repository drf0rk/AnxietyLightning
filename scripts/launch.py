# /content/ANXETY/scripts/launch.py (v8 - HEAVY DEBUGGING)

import os
import sys
from pathlib import Path
import time
import yaml
from IPython import get_ipython
import re
import shlex
import asyncio
import logging
import requests
import argparse

print("--- DEBUG: launch.py script started ---")

# --- Pathing & Settings ---
try:
    ANXETY_ROOT = Path(__file__).resolve().parents[1]
    print(f"DEBUG: ANXETY_ROOT set to {ANXETY_ROOT} from __file__")
except NameError:
    ANXETY_ROOT = Path('/content/ANXETY')
    print(f"DEBUG: ANXETY_ROOT set to {ANXETY_ROOT} as fallback")

if str(ANXETY_ROOT / 'modules') not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT / 'modules'))
    print(f"DEBUG: Added {ANXETY_ROOT / 'modules'} to sys.path")

try:
    from modules.TunnelHub import Tunnel
    import modules.json_utils as js
    print("DEBUG: Successfully imported TunnelHub and json_utils.")
except Exception as e:
    print(f"❌ DEBUG: FAILED TO IMPORT MODULES: {e}")


SETTINGS_PATH = ANXETY_ROOT / 'settings.json'
print(f"DEBUG: Settings path is {SETTINGS_PATH}")

# --- Direct & Robust Settings Loading ---
print("DEBUG: Reading settings from json...")
webui_settings = js.read(SETTINGS_PATH, 'WEBUI', {})
widget_settings = js.read(SETTINGS_PATH, 'WIDGETS', {})
env_settings = js.read(SETTINGS_PATH, 'ENVIRONMENT', {})
print("DEBUG: Settings sections read.")

if not webui_settings or not widget_settings or not env_settings:
    print("❌ DEBUG: One or more settings sections are empty. This will cause errors.")
    print(f"DEBUG: WEBUI: {webui_settings}")
    print(f"DEBUG: WIDGETS: {widget_settings}")
    print(f"DEBUG: ENVIRONMENT: {env_settings}")

# --- Explicitly Define Variables from Settings ---
HOME = Path(env_settings.get('home_path', '/content'))
print(f"DEBUG: HOME directory set to: {HOME}")

UI = webui_settings.get('current', 'Forge')
print(f"DEBUG: UI set to: {UI}")

WEBUI_PATH = Path(webui_settings.get('webui_path', str(HOME / UI)))
print(f"DEBUG: WEBUI_PATH set to: {WEBUI_PATH}")

commandline_arguments = widget_settings.get('commandline_arguments', '')
theme_accent = widget_settings.get('theme_accent', 'anxety')
ngrok_token = widget_settings.get('ngrok_token')
print("DEBUG: Variables from settings loaded.")


# --- VENV PATH ACTIVATION ---
is_classic_ui = UI == 'Classic'
python_version = 'python3.11' if is_classic_ui else 'python3.10'
VENV_PATH = HOME / 'venv'
BIN_PATH = VENV_PATH / 'bin'
PKG_PATH = VENV_PATH / f'lib/{python_version}/site-packages'

print("DEBUG: Activating VENV paths...")
if str(BIN_PATH) not in os.environ['PATH']:
    os.environ['PATH'] = f"{BIN_PATH}:{os.environ['PATH']}"
if str(PKG_PATH) not in os.environ.get('PYTHONPATH', ''):
    os.environ['PYTHONPATH'] = f"{PKG_PATH}:{os.environ.get('PYTHONPATH', '')}"
print("DEBUG: VENV paths activated.")

def get_launch_command():
    print("DEBUG: Inside get_launch_command()...")
    base_args = commandline_arguments
    if theme_accent != 'anxety' and UI != 'ComfyUI':
         base_args += f" --anxety-theme={theme_accent}"

    if UI == 'ComfyUI':
        print("DEBUG: Building command for ComfyUI.")
        return f"python3 main.py {base_args}"
    else:
        print("DEBUG: Building command for A1111-family UI.")
        command = ["python3", "launch.py"]
        if base_args:
            command.extend(shlex.split(base_args))
        
        shared_models_dir = HOME / 'sd_models_shared' / 'models'
        print(f"DEBUG: Shared models directory is: {shared_models_dir}")
        path_args = {
            "--ckpt-dir": shared_models_dir / 'Stable-diffusion',
            "--vae-dir": shared_models_dir / 'VAE',
            "--lora-dir": shared_models_dir / 'Lora',
            "--embeddings-dir": shared_models_dir / 'embeddings',
            "--controlnet-dir": shared_models_dir / 'ControlNet'
        }
        
        for arg, path in path_args.items():
            command.append(arg)
            command.append(f'"{path}"')
            
        final_command = " ".join(command)
        print(f"DEBUG: Final command string is: {final_command}")
        return final_command

# --- Main Execution ---
if __name__ == '__main__':
    print('DEBUG: Main execution block started.')
    print('Please Wait, Launching WebUI and Tunnels...\n')
    
    if not WEBUI_PATH.exists() or not WEBUI_PATH.is_dir():
        print(f"❌ FATAL ERROR: WebUI directory not found at the expected path: {WEBUI_PATH}")
        sys.exit(1)

    print(f"DEBUG: Changing directory to {WEBUI_PATH}")
    os.chdir(WEBUI_PATH)
    
    # --- Setup and Run Tunnels ---
    tunnel_port = 8188 if UI == 'ComfyUI' else 7860
    print(f"DEBUG: Setting up tunnels on port {tunnel_port}")
    tunneling_service = Tunnel(tunnel_port, debug=True)
    
    gradio_script_path = ANXETY_ROOT / '__configs__'/ 'gradio-tunneling.py'
    print(f"DEBUG: Adding Gradio tunnel with command: python3 {gradio_script_path} {tunnel_port}")
    tunneling_service.add_tunnel(
        command=f"python3 {gradio_script_path} {tunnel_port}",
        pattern=re.compile(r'https://[\w-]+\.gradio\.live'),
        name='Gradio'
    )
    
    if ngrok_token:
        print("DEBUG: Ngrok token found, adding Ngrok tunnel.")
        tunneling_service.add_tunnel(
            command=f"ngrok http {tunnel_port} --authtoken={ngrok_token} --log=stdout",
            pattern=re.compile(r'https://[a-zA-Z0-9.-]+\.ngrok-free\.app'),
            name='Ngrok'
        )
    
    print("DEBUG: Starting tunnel service (non-blocking)...")
    tunneling_service.__enter__()
    print("DEBUG: Tunnel service threads started.")

    # --- Launch WebUI Immediately ---
    LAUNCHER_COMMAND = get_launch_command()
    print(f"🚀 Launching {UI} with command: {LAUNCHER_COMMAND}")

    ipython = get_ipython()
    ipython.system_raw(f"{LAUNCHER_COMMAND} &")

    print("\n✅ WebUI and Tunnels are launching in the background.")
    print("The public URL(s) will appear above shortly as they become available.")
    print("This cell will keep running to maintain the connection. Interrupt the kernel (Stop button) to end the session.")
    print("DEBUG: launch.py script finished its main execution block.")

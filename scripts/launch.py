# /content/ANXETY/scripts/launch.py (Corrected Tunnel Logic)

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

# --- Pathing & Settings ---
try:
    ANXETY_ROOT = Path(__file__).resolve().parents[1]
except NameError:
    ANXETY_ROOT = Path('/content/ANXETY') # Fallback for some envs

if str(ANXETY_ROOT / 'modules') not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT / 'modules'))

from modules.TunnelHub import Tunnel
import modules.json_utils as js

SETTINGS_PATH = ANXETY_ROOT / 'settings.json'

# --- Direct & Robust Settings Loading ---
webui_settings = js.read(SETTINGS_PATH, 'WEBUI', {})
widget_settings = js.read(SETTINGS_PATH, 'WIDGETS', {})
env_settings = js.read(SETTINGS_PATH, 'ENVIRONMENT', {})

# --- Explicitly Define Variables from Settings ---
HOME = Path(env_settings.get('home_path', '/content'))
UI = webui_settings.get('current', 'Forge')
WEBUI_PATH = Path(webui_settings.get('webui_path', str(HOME / UI)))
commandline_arguments = widget_settings.get('commandline_arguments', '')
theme_accent = widget_settings.get('theme_accent', 'anxety')
ngrok_token = widget_settings.get('ngrok_token') # Get Ngrok token from widgets

# --- VENV PATH ACTIVATION ---
is_classic_ui = UI == 'Classic'
python_version = 'python3.11' if is_classic_ui else 'python3.10'
VENV_PATH = HOME / 'venv'
BIN_PATH = VENV_PATH / 'bin'
PKG_PATH = VENV_PATH / f'lib/{python_version}/site-packages'

if str(BIN_PATH) not in os.environ['PATH']:
    os.environ['PATH'] = f"{BIN_PATH}:{os.environ['PATH']}"
if str(PKG_PATH) not in os.environ.get('PYTHONPATH', ''):
    os.environ['PYTHONPATH'] = f"{PKG_PATH}:{os.environ.get('PYTHONPATH', '')}"

# --- Tunneling Logic ---
class TunnelManager:
    # This class is a simplified placeholder as the primary tunnel logic
    # is now handled by the imported TunnelHub and the main script body.
    pass

def get_launch_command():
    """Constructs the final launch command with all arguments."""
    base_args = commandline_arguments
    if theme_accent != 'anxety' and UI != 'ComfyUI':
         base_args += f" --anxety-theme={theme_accent}"

    if UI == 'ComfyUI':
        # Create extra_model_paths.yaml for ComfyUI
        # Paths are constructed using HOME, which is correctly set to /content
        return f"python3 main.py {base_args}"
    else:
        # A1111-family UIs use explicit path arguments
        shared_models_dir = HOME / 'sd_models_shared' / 'models'
        return (f"python3 launch.py {base_args} "
                f"--ckpt-dir \"{shared_models_dir / 'Stable-diffusion'}\" "
                f"--vae-dir \"{shared_models_dir / 'VAE'}\" "
                f"--lora-dir \"{shared_models_dir / 'Lora'}\" "
                f"--embeddings-dir \"{shared_models_dir / 'embeddings'}\" "
                f"--controlnet-dir \"{shared_models_dir / 'ControlNet'}\"")

# --- Main Execution ---
if __name__ == '__main__':
    print('Please Wait, Launching WebUI and Tunnels...\n')
    
    if not WEBUI_PATH.exists() or not WEBUI_PATH.is_dir():
        print(f"❌ FATAL ERROR: WebUI directory not found at the expected path: {WEBUI_PATH}")
        sys.exit(1)

    os.chdir(WEBUI_PATH)
    
    # --- Setup and Run Tunnels ---
    tunnel_port = 8188 if UI == 'ComfyUI' else 7860
    tunneling_service = Tunnel(tunnel_port, debug=True)

    # Add Gradio Tunnel - CORRECTED COMMAND
    gradio_script_path = ANXETY_ROOT / '__configs__'/ 'gradio-tunneling.py'
    tunneling_service.add_tunnel(
        command=f"python3 {gradio_script_path} {tunnel_port}",
        pattern=re.compile(r'https://[\w-]+\.gradio\.live'),
        name='Gradio'
    )

    # Add Ngrok Tunnel if token exists
    if ngrok_token:
        # The TunnelHub module itself should handle authtoken configuration if needed,
        # but the command is straightforward.
        tunneling_service.add_tunnel(
            command=f"ngrok http {tunnel_port} --authtoken={ngrok_token} --log=stdout",
            pattern=re.compile(r'https://[a-zA-Z0-9.-]+\.ngrok-free\.app'),
            name='Ngrok'
        )
    
    # Launch tunnels in the background
    tunneling_service.start()

    # --- Launch WebUI ---
    LAUNCHER_COMMAND = get_launch_command()
    print(f"🚀 Launching {UI} with command: {LAUNCHER_COMMAND}")

    ipython = get_ipython()
    ipython.system_raw(f"{LAUNCHER_COMMAND} &")

    print("\n✅ WebUI is launching in the background.")
    print("This cell will keep running to maintain the connection. Interrupt the kernel (Stop button) to end the session.")
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        print("\n⏹️ Cell interrupted by user. The WebUI process may still be running in the background.")

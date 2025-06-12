# /content/ANXETY/scripts/launch.py (v14 - Final Stable Version)

import os
import sys
from pathlib import Path
import time
import yaml
from IPython import get_ipython
import re
import shlex

# --- Pathing & Settings ---
try:
    ANXETY_ROOT = Path(__file__).resolve().parents[1]
except NameError:
    ANXETY_ROOT = Path('/content/ANXETY')

if str(ANXETY_ROOT / 'modules') not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT / 'modules'))

import modules.json_utils as js

SETTINGS_PATH = ANXETY_ROOT / 'settings.json'
LOG_DIR = ANXETY_ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)

# --- Load Settings ---
webui_settings = js.read(SETTINGS_PATH, 'WEBUI', {})
widget_settings = js.read(SETTINGS_PATH, 'WIDGETS', {})
env_settings = js.read(SETTINGS_PATH, 'ENVIRONMENT', {})

HOME = Path(env_settings.get('home_path', '/content'))
UI = webui_settings.get('current', 'Forge')
WEBUI_PATH = Path(webui_settings.get('webui_path', str(HOME / UI)))
commandline_arguments = widget_settings.get('commandline_arguments', '')
ngrok_token = widget_settings.get('ngrok_token')

# --- VENV PATH ACTIVATION ---
python_version = 'python3.11' if UI == 'Classic' else 'python3.10'
VENV_PATH = HOME / 'venv'
BIN_PATH = VENV_PATH / 'bin'

if str(BIN_PATH) not in os.environ['PATH']:
    os.environ['PATH'] = f"{BIN_PATH}:{os.environ['PATH']}"

def get_launch_command():
    """Constructs the final launch command with all arguments."""
    base_args = commandline_arguments
    if UI == 'ComfyUI':
        return f"python3 main.py {base_args}"
    else:
        command = ["python3", "launch.py"]
        if base_args: command.extend(shlex.split(base_args))
        shared_models_dir = HOME / 'sd_models_shared' / 'models'
        path_args = {
            "--ckpt-dir": shared_models_dir / 'Stable-diffusion',
            "--vae-dir": shared_models_dir / 'VAE',
            "--lora-dir": shared_models_dir / 'Lora',
            "--embeddings-dir": shared_models_dir / 'embeddings',
            "--controlnet-dir": shared_models_dir / 'ControlNet'
        }
        for arg, path in path_args.items():
            command.append(arg); command.append(f'"{path}"')
        return " ".join(command)

# --- Main Execution ---
if __name__ == '__main__':
    print('Please Wait, Launching WebUI and Tunnels...\n')
    
    if not WEBUI_PATH.exists():
        print(f"❌ FATAL ERROR: WebUI directory not found at {WEBUI_PATH}"); sys.exit(1)

    os.chdir(WEBUI_PATH)
    
    # --- Define Tunnel Commands & Log Files ---
    tunnel_port = 8188 if UI == 'ComfyUI' else 7860
    tunnels_to_launch = []

    # Gradio
    gradio_log = LOG_DIR / "gradio.log"
    gradio_script_path = ANXETY_ROOT / '__configs__'/ 'gradio-tunneling.py'
    tunnels_to_launch.append({
        'name': 'Gradio',
        'cmd': f"python3 {gradio_script_path} {tunnel_port}",
        'log_file': gradio_log,
        'pattern': re.compile(r'https://[\w-]+\.gradio\.live')
    })

    # Ngrok
    if ngrok_token:
        ngrok_log = LOG_DIR / "ngrok.log"
        tunnels_to_launch.append({
            'name': 'Ngrok',
            'cmd': f"ngrok http {tunnel_port} --authtoken={ngrok_token} --log=stdout",
            'log_file': ngrok_log,
            'pattern': re.compile(r'https://[a-zA-Z0-9.-]+\.ngrok-free\.app')
        })

    # Cloudflare
    cloudflare_log = LOG_DIR / "cloudflare.log"
    tunnels_to_launch.append({
        'name': 'Cloudflare',
        'cmd': f"cloudflared tunnel --url http://localhost:{tunnel_port}",
        'log_file': cloudflare_log,
        'pattern': re.compile(r'https://[a-zA-Z0-9.-]+\.trycloudflare\.com')
    })
    
    # --- Launch Tunnels & WebUI in Background ---
    ipython = get_ipython()
    
    for tunnel in tunnels_to_launch:
        print(f"🚀 Launching {tunnel['name']} tunnel... (Log: {tunnel['log_file']})")
        ipython.system_raw(f"touch {tunnel['log_file']}")
        ipython.system_raw(f"{tunnel['cmd']} > {tunnel['log_file']} 2>&1 &")

    LAUNCHER_COMMAND = get_launch_command()
    print(f"🚀 Launching {UI} with command: {LAUNCHER_COMMAND}")
    ipython.system_raw(f"{LAUNCHER_COMMAND} &")
    
    # --- Monitor Logs for URLs ---
    print("\n✅ WebUI and Tunnels are launching... Monitoring logs for public URLs...")
    
    found_urls = {}
    start_time = time.time()
    # Monitor for 3 minutes (180 seconds)
    while time.time() - start_time < 180 and len(found_urls) < len(tunnels_to_launch):
        for tunnel in tunnels_to_launch:
            if tunnel['name'] not in found_urls:
                try:
                    with open(tunnel['log_file'], 'r') as f:
                        for line in f:
                            match = tunnel['pattern'].search(line)
                            if match:
                                url = match.group(0)
                                print(f"\n--- ✅ DETECTED {tunnel['name']} URL: {url} ---")
                                found_urls[tunnel['name']] = url
                                break
                except FileNotFoundError:
                    continue
        time.sleep(5)
    
    print("\n--- Tunnel Summary ---")
    if found_urls:
        for name, url in sorted(found_urls.items()):
            print(f"🔗 {name}: {url}")
    else:
        print("❌ No public URLs were generated within the time limit.")
        print(f"Please check the log files in the {LOG_DIR} directory for errors.")

    print("\nThis cell will keep running to maintain the WebUI. Interrupt to stop.")

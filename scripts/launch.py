# /content/ANXETY/scripts/launch.py (Robust Logging Edition)

import os
import sys
from pathlib import Path
import time
import re
import shlex
import json
from IPython import get_ipython

# --- Pathing & Settings ---
ANXETY_ROOT = Path('/content/ANXETY')
if str(ANXETY_ROOT / 'modules') not in sys.path: sys.path.insert(0, str(ANXETY_ROOT / 'modules'))
import modules.json_utils as js

SETTINGS_PATH = ANXETY_ROOT / 'settings.json'
LOG_DIR = ANXETY_ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)

# --- ROBUSTNESS CHANGE: Structured JSON Logger ---
def log(level, message, data=None):
    log_entry = {"type": "log", "level": level, "message": message, "data": data or {}}
    print(json.dumps(log_entry), flush=True)

# --- Load Settings ---
try:
    settings_blob = js.read(SETTINGS_PATH)
    webui_settings = settings_blob.get('WEBUI', {})
    widget_settings = settings_blob.get('WIDGETS', {})
    env_settings = settings_blob.get('ENVIRONMENT', {})
except Exception as e:
    log('error', f"Fatal error loading settings: {e}"); sys.exit(1)

HOME = Path(env_settings.get('home_path', '/content'))
UI = webui_settings.get('current', 'Forge')
WEBUI_PATH = Path(webui_settings.get('webui_path', str(HOME / UI)))
commandline_arguments = widget_settings.get('commandline_arguments', '')
ngrok_token = widget_settings.get('ngrok_token')

def get_launch_command():
    base_args = commandline_arguments
    if UI == 'ComfyUI': return f"python3 main.py {base_args}"
    command = ["python3", "launch.py"]
    if base_args: command.extend(shlex.split(base_args))
    shared_models_dir = HOME / 'sd_models_shared' / 'models'
    path_args = {"--ckpt-dir":shared_models_dir/'Stable-diffusion',"--vae-dir":shared_models_dir/'VAE',"--lora-dir":shared_models_dir/'Lora',"--embeddings-dir":shared_models_dir/'embeddings',"--controlnet-dir":shared_models_dir/'ControlNet'}
    for arg, path in path_args.items(): command.extend([arg, f'"{path}"'])
    return " ".join(command)

if __name__ == '__main__':
    log('info', 'Please Wait, Launching WebUI and Tunnels...')
    
    if not WEBUI_PATH.exists():
        log('error', f"FATAL ERROR: WebUI directory not found at {WEBUI_PATH}"); sys.exit(1)

    os.chdir(WEBUI_PATH)
    
    tunnel_port = 8188 if UI == 'ComfyUI' else 7860
    tunnels_to_launch = [
        {'name':'Gradio','cmd':f"python3 {ANXETY_ROOT/'__configs__'/'gradio-tunneling.py'} {tunnel_port}",'log_file':LOG_DIR/"gradio.log",'pattern':re.compile(r'https://[\w-]+\.gradio\.live')},
        {'name':'Cloudflare','cmd':f"cloudflared tunnel --url http://localhost:{tunnel_port}",'log_file':LOG_DIR/"cloudflare.log",'pattern':re.compile(r'https://[a-zA-Z0-9.-]+\.trycloudflare\.com')}
    ]
    if ngrok_token:
        tunnels_to_launch.append({'name':'Ngrok','cmd':f"ngrok http {tunnel_port} --authtoken={ngrok_token} --log=stdout",'log_file':LOG_DIR/"ngrok.log",'pattern':re.compile(r'https://[a-zA-Z0-9.-]+\.ngrok-free\.app')})
    
    ipython = get_ipython()
    for tunnel in tunnels_to_launch:
        log('info', f"🚀 Launching {tunnel['name']} tunnel...")
        ipython.system_raw(f"{tunnel['cmd']} > \"{tunnel['log_file']}\" 2>&1 &")

    LAUNCHER_COMMAND = get_launch_command()
    log('info', f"🚀 Launching {UI} with command: {LAUNCHER_COMMAND}")
    ipython.system_raw(f"{LAUNCHER_COMMAND} &")
    
    log('header', "--- Monitoring logs for public URLs... ---")
    
    found_urls = {}
    start_time = time.time()
    while time.time() - start_time < 180 and len(found_urls) < len(tunnels_to_launch):
        for tunnel in tunnels_to_launch:
            if tunnel['name'] not in found_urls:
                try:
                    with open(tunnel['log_file'], 'r') as f:
                        for line in f:
                            if match := tunnel['pattern'].search(line):
                                url = match.group(0)
                                # ROBUSTNESS CHANGE: Use specific level for URLs
                                log('url', f"🔗 {tunnel['name']}: {url}")
                                found_urls[tunnel['name']] = url
                                break
                except FileNotFoundError: continue
        time.sleep(5)
    
    if not found_urls:
        log('error', "❌ No public URLs were generated within the time limit. Please check logs for errors.")

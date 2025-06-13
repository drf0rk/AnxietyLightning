# /content/ANXETY/scripts/launch.py (vRobust - Backend Fixes v2)

import os
import sys
from pathlib import Path
import time
import re
import shlex
import json
import subprocess

# --- Self-Contained Path Setup ---
try:
    ANXETY_ROOT_BACKEND = Path(__file__).resolve().parents[1]
except NameError:
    ANXETY_ROOT_BACKEND = Path('/content/ANXETY')

if str(ANXETY_ROOT_BACKEND) not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT_BACKEND))
# --- End Self-Contained Path Setup ---

import modules.json_utils as js

SETTINGS_PATH = ANXETY_ROOT_BACKEND / 'settings.json'
LOG_DIR = ANXETY_ROOT_BACKEND / "logs"
LOG_DIR.mkdir(exist_ok=True)

def log(level, message, data=None):
    log_entry = {"type": "log", "level": level, "message": message, "data": data or {}}
    print(json.dumps(log_entry), flush=True)

try:
    settings_blob = js.read(SETTINGS_PATH)
    webui_settings = settings_blob.get('WEBUI', {})
    widget_settings = settings_blob.get('WIDGETS', {})
    env_settings = settings_blob.get('ENVIRONMENT', {})
except Exception as e:
    log('error', f"Fatal error loading settings in launch.py: {e}"); sys.exit(1)

HOME = Path(env_settings.get('home_path', '/content'))
UI = widget_settings.get('change_webui', 'Forge') # Get current UI from WIDGETS
# Construct the WEBUI_PATH based on the UI selected by the user
WEBUI_PATH = HOME / UI 

commandline_arguments = widget_settings.get('commandline_arguments', '')
ngrok_token = widget_settings.get('ngrok_token')

def get_launch_command():
    base_args = commandline_arguments
    # ComfyUI uses 'main.py', others use 'launch.py'
    script_to_run = "main.py" if UI == 'ComfyUI' else "launch.py"
    command = ["python3", script_to_run] # Use the determined script

    if base_args: command.extend(shlex.split(base_args))
    
    # Path arguments are generally not needed for ComfyUI's main.py
    if UI != 'ComfyUI':
        shared_models_dir = HOME / 'sd_models_shared' / 'models'
        path_args = {
            "--ckpt-dir":shared_models_dir/'Stable-diffusion',
            "--vae-dir":shared_models_dir/'VAE',
            "--lora-dir":shared_models_dir/'Lora',
            "--embeddings-dir":shared_models_dir/'embeddings',
            "--controlnet-dir":shared_models_dir/'ControlNet'
        }
        for arg, path_val in path_args.items(): # Renamed path to path_val
            command.extend([arg, f'"{path_val}"'])
    return " ".join(command)

if __name__ == '__main__':
    log('info', 'Please Wait, Launching WebUI and Tunnels...')
    
    if not WEBUI_PATH.exists():
        log('error', f"FATAL ERROR: WebUI directory not found at {WEBUI_PATH}. This usually means the downloading-en.py script failed."); sys.exit(1)

    os.chdir(WEBUI_PATH) # Change to the WebUI directory to run its launch script
    
    tunnel_port = 8188 if UI == 'ComfyUI' else 7860
    tunnels_to_launch = [
        {'name':'Gradio','cmd':f"python3 {ANXETY_ROOT_BACKEND/'__configs__'/'gradio-tunneling.py'} {tunnel_port}",'log_file':LOG_DIR/"gradio.log",'pattern':re.compile(r'https://[\w-]+\.gradio\.live')},
        {'name':'Cloudflare','cmd':f"cloudflared tunnel --url http://localhost:{tunnel_port}",'log_file':LOG_DIR/"cloudflare.log",'pattern':re.compile(r'https://[a-zA-Z0-9.-]+\.trycloudflare\.com')}
    ]
    if ngrok_token:
        tunnels_to_launch.append({'name':'Ngrok','cmd':f"ngrok http {tunnel_port} --authtoken={ngrok_token} --log=stdout",'log_file':LOG_DIR/"ngrok.log",'pattern':re.compile(r'https://[a-zA-Z0-9.-]+\.ngrok-free\.app')})
    
    for tunnel in tunnels_to_launch:
        log('info', f"🚀 Launching {tunnel['name']} tunnel...")
        with open(tunnel['log_file'], 'wb') as log_file_handle:
             subprocess.Popen(shlex.split(tunnel['cmd']), stdout=log_file_handle, stderr=subprocess.STDOUT)

    LAUNCHER_COMMAND = get_launch_command()
    log('info', f"🚀 Launching {UI} with command: {LAUNCHER_COMMAND}")
    # Log WebUI output to its own file for easier debugging
    webui_output_log_file = LOG_DIR / f"{UI}_launch_output.log"
    with open(webui_output_log_file, 'wb') as webui_log_handle:
        subprocess.Popen(shlex.split(LAUNCHER_COMMAND), stdout=webui_log_handle, stderr=subprocess.STDOUT)
    
    log('header', "--- Monitoring logs for public URLs... ---")
    
    found_urls = {}
    start_time = time.time()
    monitoring_duration = 180 
    all_urls_found_flag = False

    while time.time() - start_time < monitoring_duration:
        all_urls_found_flag = True 
        for tunnel in tunnels_to_launch:
            if tunnel['name'] not in found_urls:
                all_urls_found_flag = False 
                try:
                    if tunnel['log_file'].exists() and tunnel['log_file'].stat().st_size > 0:
                        with open(tunnel['log_file'], 'r', encoding='utf-8', errors='replace') as f:
                            for line_content in f: 
                                if match := tunnel['pattern'].search(line_content):
                                    url = match.group(0)
                                    log('url', f"🔗 {tunnel['name']}: {url}")
                                    found_urls[tunnel['name']] = url
                                    break 
                except FileNotFoundError: pass
                except Exception as e: log('error', f"Error reading log for {tunnel['name']}: {e}")
        
        if all_urls_found_flag and len(found_urls) == len(tunnels_to_launch):
            log('success', "✅ All tunnel URLs detected.")
            break 
        time.sleep(5) 
    
    if not found_urls:
        log('error', "❌ No public URLs were generated within the time limit. Please check individual log files in the 'logs' directory for errors.")
    elif not all_urls_found_flag:
        log('warning', "⚠️ Not all tunnel URLs were detected. Some tunnels may have failed. Check logs.")
    
    # The script will naturally exit after this, as Popen launched background processes.
    # The Gradio UI in the notebook will show the "Process Complete" message.

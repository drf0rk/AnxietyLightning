# /content/ANXETY/scripts/launch.py (vRobust - Backend Fixes)

import os
import sys
from pathlib import Path
import time
import re
import shlex
import json
import subprocess # Added for Popen

# --- Self-Contained Path Setup ---
try:
    ANXETY_ROOT_BACKEND = Path(__file__).resolve().parents[1] # Adjust if path changes
except NameError:
    ANXETY_ROOT_BACKEND = Path('/content/ANXETY')

if str(ANXETY_ROOT_BACKEND) not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT_BACKEND))
# --- End Self-Contained Path Setup ---

import modules.json_utils as js # This import should now work

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
        {'name':'Gradio','cmd':f"python3 {ANXETY_ROOT_BACKEND/'__configs__'/'gradio-tunneling.py'} {tunnel_port}",'log_file':LOG_DIR/"gradio.log",'pattern':re.compile(r'https://[\w-]+\.gradio\.live')},
        {'name':'Cloudflare','cmd':f"cloudflared tunnel --url http://localhost:{tunnel_port}",'log_file':LOG_DIR/"cloudflare.log",'pattern':re.compile(r'https://[a-zA-Z0-9.-]+\.trycloudflare\.com')}
    ]
    if ngrok_token:
        tunnels_to_launch.append({'name':'Ngrok','cmd':f"ngrok http {tunnel_port} --authtoken={ngrok_token} --log=stdout",'log_file':LOG_DIR/"ngrok.log",'pattern':re.compile(r'https://[a-zA-Z0-9.-]+\.ngrok-free\.app')})
    
    for tunnel in tunnels_to_launch:
        log('info', f"🚀 Launching {tunnel['name']} tunnel...")
        with open(tunnel['log_file'], 'wb') as log_file_handle: # Open in binary write mode for Popen
             subprocess.Popen(shlex.split(tunnel['cmd']), stdout=log_file_handle, stderr=subprocess.STDOUT)


    LAUNCHER_COMMAND = get_launch_command()
    log('info', f"🚀 Launching {UI} with command: {LAUNCHER_COMMAND}")
    with open(LOG_DIR / f"{UI}_launch.log", 'wb') as webui_log_handle: # Open in binary write mode
        subprocess.Popen(shlex.split(LAUNCHER_COMMAND), stdout=webui_log_handle, stderr=subprocess.STDOUT)
    
    log('header', "--- Monitoring logs for public URLs... ---")
    
    found_urls = {}
    start_time = time.time()
    # Increased timeout for tunnel startup, e.g., 3 minutes (180 seconds)
    # For initial launch, we might need longer if the WebUI itself takes time to start.
    # Gradio UI progress will show the actual WebUI log.
    monitoring_duration = 180 
    all_urls_found_flag = False

    while time.time() - start_time < monitoring_duration:
        all_urls_found_flag = True # Assume all found until proven otherwise
        for tunnel in tunnels_to_launch:
            if tunnel['name'] not in found_urls:
                all_urls_found_flag = False # At least one is still missing
                try:
                    # Check if log file exists and is not empty
                    if tunnel['log_file'].exists() and tunnel['log_file'].stat().st_size > 0:
                        with open(tunnel['log_file'], 'r', encoding='utf-8', errors='replace') as f:
                            for line_content in f: # Iterate through lines
                                if match := tunnel['pattern'].search(line_content):
                                    url = match.group(0)
                                    log('url', f"🔗 {tunnel['name']}: {url}")
                                    found_urls[tunnel['name']] = url
                                    break # Found URL for this tunnel, move to next
                except FileNotFoundError:
                    pass # Log file might not be created yet
                except Exception as e:
                    log('error', f"Error reading log for {tunnel['name']}: {e}")
        
        if all_urls_found_flag and len(found_urls) == len(tunnels_to_launch):
            log('success', "✅ All tunnel URLs detected.")
            break 
        time.sleep(5) 
    
    if not found_urls:
        log('error', "❌ No public URLs were generated within the time limit. Please check individual log files in the 'logs' directory for errors.")
    elif not all_urls_found_flag:
        log('warning', "⚠️ Not all tunnel URLs were detected within the time limit. Some tunnels may have failed to start.")

    # Keep launch.py alive to keep tunnels and WebUI running until user stops the cell.
    # The Gradio UI will show a "Process Complete" message.
    # This script's purpose is primarily to launch and report initial URLs.
    # The main UI continues in the notebook cell where Gradio is running.
    # log('info', "Backend launch script finished. WebUI and tunnels should be running in the background.")

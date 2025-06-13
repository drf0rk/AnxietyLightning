# /content/ANXETY/scripts/launch.py (vRobust - Force VENV for WebUI)

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

# --- CRITICAL: Define VENV Python Path ---
# This must align with the VENV installed by downloading-en.py
COLAB_CONTENT_PATH = Path(env_settings.get('home_path', '/content')) # Should be /content
VENV_PYTHON_EXECUTABLE = COLAB_CONTENT_PATH / "venv" / "bin" / "python3"
# ---

UI = widget_settings.get('change_webui', 'Forge')
WEBUI_PATH = COLAB_CONTENT_PATH / UI 
commandline_arguments = widget_settings.get('commandline_arguments', '')
ngrok_token = widget_settings.get('ngrok_token')

def get_launch_command():
    base_args = commandline_arguments
    
    # Determine the correct Python executable from our VENV
    python_exe = str(VENV_PYTHON_EXECUTABLE)
    if not VENV_PYTHON_EXECUTABLE.exists():
        log('warning', f"VENV Python not found at {VENV_PYTHON_EXECUTABLE}, falling back to system python3. WebUI might have issues.")
        python_exe = "python3" # Fallback, but likely problematic

    webui_script_to_run = "main.py" if UI == 'ComfyUI' else "launch.py"
    
    # command = [python_exe, webui_script_to_run] # Start with VENV python and UI's launch script
    # Prepend PYTHONNOUSERSITE=1 to prevent global site packages from interfering
    command_prefix = ["env", "PYTHONNOUSERSITE=1", python_exe, webui_script_to_run]
    command = command_prefix


    if base_args: command.extend(shlex.split(base_args))
    
    if UI != 'ComfyUI':
        # These paths point to the shared model structure, which is correct.
        shared_models_dir = COLAB_CONTENT_PATH / 'sd_models_shared' / 'models'
        path_args = {
            "--ckpt-dir":shared_models_dir/'Stable-diffusion',
            "--vae-dir":shared_models_dir/'VAE',
            "--lora-dir":shared_models_dir/'Lora',
            "--embeddings-dir":shared_models_dir/'embeddings',
            "--controlnet-dir":shared_models_dir/'ControlNet'
        }
        for arg, path_val in path_args.items():
            command.extend([arg, f'"{path_val}"'])
    
    # Return as a list for Popen, not a string, to avoid shell=True issues.
    return command


if __name__ == '__main__':
    log('info', 'Please Wait, Launching WebUI and Tunnels...')
    
    if not WEBUI_PATH.exists():
        log('error', f"FATAL ERROR: WebUI directory not found at {WEBUI_PATH}. This usually means the downloading-en.py script failed."); sys.exit(1)

    # No need to os.chdir(WEBUI_PATH) if launch.py is called with its full path
    # and its internal paths are relative or also absolute.
    # However, many launch.py scripts assume they are run from their own directory.
    # So, changing directory is safer.
    os.chdir(WEBUI_PATH) 
    
    tunnel_port = 8188 if UI == 'ComfyUI' else 7860
    tunnels_to_launch = [
        {'name':'Gradio','cmd':f"{sys.executable} {ANXETY_ROOT_BACKEND/'__configs__'/'gradio-tunneling.py'} {tunnel_port}",'log_file':LOG_DIR/"gradio.log",'pattern':re.compile(r'https://[\w-]+\.gradio\.live')},
        {'name':'Cloudflare','cmd':f"cloudflared tunnel --url http://localhost:{tunnel_port}",'log_file':LOG_DIR/"cloudflare.log",'pattern':re.compile(r'https://[a-zA-Z0-9.-]+\.trycloudflare\.com')}
    ]
    if ngrok_token:
        tunnels_to_launch.append({'name':'Ngrok','cmd':f"ngrok http {tunnel_port} --authtoken={ngrok_token} --log=stdout",'log_file':LOG_DIR/"ngrok.log",'pattern':re.compile(r'https://[a-zA-Z0-9.-]+\.ngrok-free\.app')})
    
    for tunnel in tunnels_to_launch:
        log('info', f"🚀 Launching {tunnel['name']} tunnel...")
        with open(tunnel['log_file'], 'wb') as log_file_handle:
             subprocess.Popen(shlex.split(tunnel['cmd']), stdout=log_file_handle, stderr=subprocess.STDOUT)

    LAUNCHER_COMMAND_LIST = get_launch_command() # Now returns a list
    log('info', f"🚀 Launching {UI} with command: {' '.join(LAUNCHER_COMMAND_LIST)}") # Log the joined string for readability
    
    webui_output_log_file = LOG_DIR / f"{UI}_launch_output.log"
    with open(webui_output_log_file, 'wb') as webui_log_handle:
        # Pass the command as a list to Popen
        subprocess.Popen(LAUNCHER_COMMAND_LIST, stdout=webui_log_handle, stderr=subprocess.STDOUT, cwd=WEBUI_PATH) 
    
    log('header', "--- Monitoring logs for public URLs... ---")
    # ... (rest of URL monitoring logic remains the same) ...
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
        
        if all_urls_found_flag and len(found_urls) == len(tunnels_to_launch) and len(tunnels_to_launch) > 0 : # ensure tunnels_to_launch is not empty
            log('success', "✅ All tunnel URLs detected.")
            break 
        elif len(tunnels_to_launch) == 0: # No tunnels were configured to launch
             log('info', "No tunnels configured to launch.")
             break
        time.sleep(5) 
    
    if not found_urls and len(tunnels_to_launch) > 0:
        log('error', "❌ No public URLs were generated within the time limit. Please check individual log files in the 'logs' directory for errors.")
    elif not all_urls_found_flag and len(tunnels_to_launch) > 0:
        log('warning', "⚠️ Not all tunnel URLs were detected. Some tunnels may have failed. Check logs.")

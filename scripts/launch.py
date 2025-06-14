# /content/ANXETY/scripts/launch.py (vRobust - Correct Log Scope)

import os
import sys
from pathlib import Path
import time
import re
import shlex
import json
import subprocess
import importlib

# --- Global Logging Function ---
def log(level, message, data=None):
    print(json.dumps({"type": "log", "level": level, "message": message, "data": data or {}}), flush=True)

# --- Self-Contained Path Setup ---
try:
    ANXETY_ROOT_BACKEND = Path(__file__).resolve().parents[1]
except NameError:
    ANXETY_ROOT_BACKEND = Path('/content/ANXETY')

if str(ANXETY_ROOT_BACKEND) not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT_BACKEND))
# --- End Self-Contained Path Setup ---

# --- CRITICAL: Force Module Reload Block ---
try:
    import modules.json_utils as json_utils_module
    importlib.reload(json_utils_module)
    js = json_utils_module
    log('debug', "Successfully reloaded json_utils module in launch.py.")
except ImportError as e:
    log('error', f"Initial import of json_utils failed in launch.py: {e}")
    import modules.json_utils as js
# --- End Reload Block ---

SETTINGS_PATH = ANXETY_ROOT_BACKEND / 'settings.json'
LOG_DIR = ANXETY_ROOT_BACKEND / "logs"
LOG_DIR.mkdir(exist_ok=True)

try:
    settings_blob = js.read(SETTINGS_PATH)
    webui_settings = settings_blob.get('WEBUI', {})
    widget_settings = settings_blob.get('WIDGETS', {})
    env_settings = settings_blob.get('ENVIRONMENT', {})
except Exception as e:
    log('error', f"Fatal error loading settings in launch.py: {e}"); sys.exit(1)

COLAB_CONTENT_PATH = Path(env_settings.get('home_path', '/content'))
VENV_PYTHON_EXECUTABLE = COLAB_CONTENT_PATH / "venv" / "bin" / "python3"

UI = widget_settings.get('change_webui', 'Forge')
WEBUI_PATH = COLAB_CONTENT_PATH / UI
commandline_arguments = widget_settings.get('commandline_arguments', '')
ngrok_token = widget_settings.get('ngrok_token')

def get_launch_command():
    base_args = commandline_arguments
    
    python_exe = str(VENV_PYTHON_EXECUTABLE)
    if not VENV_PYTHON_EXECUTABLE.exists():
        log('warning', f"VENV Python not found at {VENV_PYTHON_EXECUTABLE}, falling back to system python3.")
        python_exe = "python3"

    webui_script_to_run = "main.py" if UI == 'ComfyUI' else "launch.py"
    
    command_prefix = ["env", "PYTHONNOUSERSITE=1", python_exe, webui_script_to_run]
    command = command_prefix

    if base_args: command.extend(shlex.split(base_args))
    
    if UI != 'ComfyUI':
        shared_models_dir = COLAB_CONTENT_PATH / 'sd_models_shared' / 'models'
        path_args = {
            "--ckpt-dir": str(shared_models_dir/'Stable-diffusion'),
            "--vae-dir": str(shared_models_dir/'VAE'),
            "--lora-dir": str(shared_models_dir/'Lora'),
            "--embeddings-dir": str(shared_models_dir/'embeddings'),
            "--controlnet-dir": str(shared_models_dir/'ControlNet')
        }
        for arg, path_val in path_args.items():
            command.extend([arg, path_val])
    
    return command

if __name__ == '__main__':
    log('info', 'Please Wait, Launching WebUI and Tunnels...')
    
    # --- Resilient WebUI Path Handling ---
    # The "happy path" - the archive was well-structured with a top-level folder.
    if WEBUI_PATH.exists() and WEBUI_PATH.is_dir():
        log('info', f"Standard WebUI directory found at: {WEBUI_PATH}")
        os.chdir(WEBUI_PATH)
    # The "fallback path" - the archive dumped its contents directly into /content.
    elif (COLAB_CONTENT_PATH / 'launch.py').exists():
        log('warning', f"Standard WebUI directory not found. Falling back to parent directory: {COLAB_CONTENT_PATH}")
        WEBUI_PATH = COLAB_CONTENT_PATH
        os.chdir(WEBUI_PATH)
    # If neither path is valid, then it's a true failure.
    else:
        log('error', f"FATAL ERROR: Could not find a valid WebUI launch script at the expected path ({WEBUI_PATH}) or in the fallback path ({(COLAB_CONTENT_PATH / 'launch.py')}). Download or extraction likely failed."); sys.exit(1)

    tunnel_port = 8188 if UI == 'ComfyUI' else 7860
    tunnels_to_launch = [
        {'name':'Gradio','cmd':f"{sys.executable} {ANXETY_ROOT_BACKEND/'__configs__'/'gradio-tunneling.py'} {tunnel_port}",'log_file':LOG_DIR/"gradio.log",'pattern':re.compile(r'https://[\\\\w-]+\\\\.gradio\\\\.live')},
        {'name':'Cloudflare','cmd':f"cloudflared tunnel --url http://localhost:{tunnel_port}",'log_file':LOG_DIR/"cloudflare.log",'pattern':re.compile(r'https://[a-zA-Z0-9.-]+\\\\.trycloudflare\\\\.com')}
    ]
    if ngrok_token:
        tunnels_to_launch.append({'name':'Ngrok','cmd':f"ngrok http {tunnel_port} --authtoken={ngrok_token} --log=stdout",'log_file':LOG_DIR/"ngrok.log",'pattern':re.compile(r'https://[a-zA-Z0-9.-]+\\\\.ngrok-free\\\\.app')})
    
    for tunnel in tunnels_to_launch:
        log('info', f"🚀 Launching {tunnel['name']} tunnel...")
        with open(tunnel['log_file'], 'wb') as log_file_handle:
             subprocess.Popen(shlex.split(tunnel['cmd']), stdout=log_file_handle, stderr=subprocess.STDOUT)

    LAUNCHER_COMMAND_LIST = get_launch_command()
    log('info', f"🚀 Launching {UI} with command: {' '.join(LAUNCHER_COMMAND_LIST)}")
    
    webui_output_log_file = LOG_DIR / f"{UI}_launch_output.log"
    with open(webui_output_log_file, 'wb') as webui_log_handle:
        subprocess.Popen(LAUNCHER_COMMAND_LIST, stdout=webui_log_handle, stderr=subprocess.STDOUT, cwd=WEBUI_Path) 
    
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
        
        if all_urls_found_flag and len(found_urls) == len(tunnels_to_launch) and len(tunnels_to_launch) > 0:
            log('success', "✅ All tunnel URLs detected.")
            break 
        elif len(tunnels_to_launch) == 0:
             log('info', "No tunnels configured to launch.")
             break
        time.sleep(5) 
    
    if not found_urls and len(tunnels_to_launch) > 0:
        log('error', "❌ No public URLs were generated within the time limit.")
    elif not all_urls_found_flag and len(tunnelels_to_launch) > 0:
        log('warning', "⚠️ Not all tunnel URLs were detected.")
# /content/ANXETY/scripts/en/downloading-en.py (vRobust - Backend Fixes)

import os
import sys
from pathlib import Path
import subprocess
import json
import shutil
from urllib.parse import urlparse, unquote
import runpy

# --- Self-Contained Path Setup ---
# This ensures the script can find the 'modules' directory when run by subprocess
try:
    ANXETY_ROOT_BACKEND = Path(__file__).resolve().parents[2] # Adjust if path changes
except NameError:
    ANXETY_ROOT_BACKEND = Path('/content/ANXETY')

if str(ANXETY_ROOT_BACKEND) not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT_BACKEND))
# --- End Self-Contained Path Setup ---

import modules.json_utils as js # This import should now work
from modules.Manager import m_download

SETTINGS_PATH = ANXETY_ROOT_BACKEND / 'settings.json'

def log(level, message, data=None):
    log_entry = {"type": "log", "level": level, "message": message, "data": data or {}}
    print(json.dumps(log_entry), flush=True)

def load_all_settings(path):
    try:
        settings_blob = js.read(path)
        return settings_blob.get('ENVIRONMENT', {}), settings_blob.get('WIDGETS', {}), settings_blob.get('WEBUI', {})
    except Exception as e:
        log('error', f'Failed to load settings: {e}')
        return {}, {}, {}

env_settings, widget_settings, webui_settings = load_all_settings(SETTINGS_PATH)
HOME = Path(env_settings.get('home_path', '/content'))
VENV_PATH = HOME / 'venv'
UI_NAME = widget_settings.get('change_webui', 'Forge')
WEBUI_PATH = Path(webui_settings.get('webui_path', str(HOME / UI_NAME)))
UI_ZIPS = {"A1111":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/A1111.zip","Forge":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/Forge.zip","ReForge":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/ReForge.zip","Classic":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/Classic.zip","ComfyUI":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/ComfyUI.zip","SD-UX":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/SD-UX.zip"}

def install_system_deps():
    log('header', 'Checking system dependencies...')
    common_deps = ['aria2', 'lz4', 'pv']
    tunnel_deps = ['ngrok', 'cloudflared'] # We can try installing these separately if needed
    
    missing_common = [pkg for pkg in common_deps if not shutil.which(pkg)]
    # For ngrok and cloudflared, checking shutil.which might not be enough if they are just downloaded binaries
    # A more robust check would be to see if the binary exists in a known PATH location.
    # For simplicity here, we'll attempt installation if they are "missing".

    if not missing_common and shutil.which('ngrok') and shutil.which('cloudflared'):
        log('success', '✅ All essential system dependencies appear to be installed.')
        return True

    log('info', f'🔧 Attempting to install/update system dependencies...')
    try:
        # Always run update first
        subprocess.run(["apt-get", "update", "-y", "-qq"], check=True, capture_output=True)
        
        if missing_common:
            log('info', f'Installing: {", ".join(missing_common)}')
            subprocess.run(["apt-get", "install", "-y", "-qq"] + missing_common, check=True, capture_output=True)

        # Special handling for cloudflared if not found by apt
        if not shutil.which('cloudflared'):
            log('info', 'Installing cloudflared manually...')
            subprocess.run(shlex.split("wget -qO /usr/local/bin/cloudflared https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64"), check=True, capture_output=True)
            subprocess.run(["chmod", "+x", "/usr/local/bin/cloudflared"], check=True, capture_output=True)

        # Special handling for ngrok if not found by apt
        if not shutil.which('ngrok'):
            log('info', 'Installing ngrok manually...')
            subprocess.run(shlex.split("wget -qO ngrok.tgz https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz"), check=True, capture_output=True)
            subprocess.run(shlex.split("tar -xzf ngrok.tgz -C /usr/local/bin"), check=True, capture_output=True) # Install to a common PATH dir
            if Path("ngrok.tgz").exists(): Path("ngrok.tgz").unlink()


        log('success', '✅ System dependency installation/update process complete.')
        return True
    except subprocess.CalledProcessError as e:
        error_detail = e.stderr.decode() if e.stderr else str(e)
        log('error', f'❌ Failed during system dependency installation: {error_detail}')
        return False
    except Exception as e:
        log('error', f'❌ An unexpected error occurred installing system dependencies: {e}')
        return False

def check_and_install_venv():
    is_classic_ui = (UI_NAME == 'Classic')
    required_venv_type = 'Classic' if is_classic_ui else 'Standard'
    installed_venv_type = env_settings.get('venv_type')

    if VENV_PATH.exists() and installed_venv_type == required_venv_type:
        log('info', '✅ Correct VENV already exists.')
        return
        
    if VENV_PATH.exists():
        log('info', '🗑️ VENV type changed or corrupted. Removing old VENV...')
        shutil.rmtree(VENV_PATH)

    venv_url, py_ver = ("https://huggingface.co/NagisaNao/ANXETY/resolve/main/python31112-venv-torch251-cu121-C-Classic.tar.lz4", '3.11.12') if required_venv_type == 'Classic' else ("https://huggingface.co/NagisaNao/ANXETY/resolve/main/python31017-venv-torch251-cu121-C-fca.tar.lz4", '3.10.17')
    log('info', f'♻️ Installing VENV ({py_ver}). This will take time...')
    
    filename = Path(urlparse(venv_url).path).name
    m_download(f'"{venv_url}" "{HOME}" "{filename}"', log=True) # m_download now uses log() internally
    if not (HOME / filename).exists():
        log('error', f'❌ VENV download failed for {filename}.'); sys.exit(1)

    log('info', '📦 Unpacking VENV...')
    try:
        subprocess.run(f"pv \"{HOME / filename}\" | lz4 -d | tar xf -", shell=True, check=True, cwd=HOME, capture_output=True)
        (HOME / filename).unlink()
        js.save(str(SETTINGS_PATH), 'ENVIRONMENT.venv_type', required_venv_type)
        log('success', '✅ VENV setup complete.')
    except Exception as e:
        log('error', f'❌ VENV unpacking failed: {e}'); sys.exit(1)

def install_webui():
    if WEBUI_PATH.exists():
        log('info', f'✅ WebUI directory for {UI_NAME} found.')
        return
    log('info', f'📦 Unpacking Stable Diffusion | WEBUI: {UI_NAME}...')
    repo_url = UI_ZIPS.get(UI_NAME)
    if not repo_url: log('error', f'❌ No download URL for UI: {UI_NAME}'); sys.exit(1)
    
    zip_path = HOME / f"{UI_NAME}.zip"
    m_download(f'"{repo_url}" "{HOME}" "{zip_path.name}"', log=True)
    if not zip_path.exists(): log('error', f'❌ Download failed for {UI_NAME}.zip'); sys.exit(1)
    
    try:
        WEBUI_PATH.mkdir(parents=True, exist_ok=True)
        subprocess.run(['unzip', '-q', '-o', str(zip_path), '-d', str(WEBUI_PATH)], check=True, capture_output=True)
        zip_path.unlink()
        log('success', f'✅ {UI_NAME} installation complete!')
    except Exception as e:
        log('error', f'❌ Unzip failed for {UI_NAME}: {e}'); sys.exit(1)

def process_asset_downloads():
    log('header', "--- Processing Asset Downloads ---")
    is_xl = widget_settings.get("sdxl_toggle", False)
    
    sd_data = runpy.run_path(str(ANXETY_ROOT_BACKEND/'scripts'/('_xl-models-data.py' if is_xl else '_models-data.py')))
    loras_data_full = runpy.run_path(str(ANXETY_ROOT_BACKEND/'scripts'/'_loras-data.py'))
    
    model_data = sd_data.get('sdxl_models_data' if is_xl else 'sd15_model_data', {})
    vae_data = sd_data.get('sdxl_vae_data' if is_xl else 'sd15_vae_data', {})
    lora_data = loras_data_full.get('lora_data', {}).get('sdxl_loras' if is_xl else 'sd15_loras', {})
    cnet_data = sd_data.get('controlnet_list', {})

    path_map = {'model':webui_settings.get('model_dir'),'vae':webui_settings.get('vae_dir'),'lora':webui_settings.get('lora_dir'),'control':webui_settings.get('control_dir')}
    
    selections = {
        'model': (widget_settings.get('model_list', []), model_data),
        'vae': (widget_settings.get('vae_list', []), vae_data),
        'lora': (widget_settings.get('lora_list', []), lora_data),
        'control': (widget_settings.get('controlnet_list', []), cnet_data)
    }
    
    download_queue = []
    for prefix, (selected_items, data_dict) in selections.items():
        for item_name in selected_items: # selected_items is a list of keys
            if item_name in data_dict:
                item_list_from_data = data_dict[item_name]
                actual_item_list = item_list_from_data if isinstance(item_list_from_data, list) else [item_list_from_data]
                for item_info in actual_item_list:
                    if isinstance(item_info, dict) and 'url' in item_info:
                        file_name = item_info.get('name') or unquote(Path(urlparse(item_info['url']).path).name)
                        dst_dir = path_map.get(prefix)
                        if dst_dir:
                            download_queue.append({'url': item_info['url'], 'dst': dst_dir, 'name': file_name, 'prefix': prefix})

    if not download_queue:
        log('info', 'ℹ️ No assets were selected for download.')
        return

    log('info', f'📦 Orchestrating downloads for {len(download_queue)} assets...')
    detailed_on = widget_settings.get('detailed_download', False)
    for i, item in enumerate(download_queue):
        if detailed_on: log('info', f"⬇️ ({i+1}/{len(download_queue)}) Queuing: {item['name']} (Type: {item['prefix']}) to {Path(item['dst']).name}")
        
        # Send progress update for Gradio
        log('progress', f"Downloading ({item['prefix']}) {item['name']}", data={'percentage': int((i / len(download_queue)) * 100)})
        
        m_download(f"\"{item['url']}\" \"{item['dst']}\" \"{item['name']}\"", log=True) # m_download should also use log()
    
    log('progress', "All downloads complete.", data={'percentage': 100})
    log('success', '✅ Download processing complete!')

if __name__ == '__main__':
    log('header', "--- Starting Environment Setup ---")
    if install_system_deps():
        check_and_install_venv()
        install_webui()
        process_asset_downloads()
    log('header', "--- ✅ Environment Setup Complete ---")

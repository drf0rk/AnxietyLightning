# /content/ANXETY/scripts/en/downloading-en.py (vRobust - Backend Fixes v3 - VENV Path)

import os
import sys
from pathlib import Path
import subprocess
import json
import shutil
from urllib.parse import urlparse, unquote
import runpy
import shlex

# --- Self-Contained Path Setup ---
try:
    ANXETY_ROOT_BACKEND = Path(__file__).resolve().parents[2]
except NameError:
    ANXETY_ROOT_BACKEND = Path('/content/ANXETY')

if str(ANXETY_ROOT_BACKEND) not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT_BACKEND))
# --- End Self-Contained Path Setup ---

import modules.json_utils as js
from modules.Manager import m_download

SETTINGS_PATH = ANXETY_ROOT_BACKEND / 'settings.json'

def log(level, message, data=None):
    log_entry = {"type": "log", "level": level, "message": message, "data": data or {}}
    print(json.dumps(log_entry), flush=True)

def load_all_settings(path):
    try:
        settings_blob = js.read(path)
        # Ensure 'ENVIRONMENT.home_path' is set to '/content' by default if not present
        env_data = settings_blob.get('ENVIRONMENT', {})
        if 'home_path' not in env_data:
            env_data['home_path'] = '/content' # Default for Colab
        
        return env_data, settings_blob.get('WIDGETS', {}), settings_blob.get('WEBUI', {})
    except Exception as e:
        log('error', f'Failed to load settings: {e}')
        return {'home_path': '/content'}, {}, {} # Ensure home_path default

env_settings, widget_settings, webui_settings = load_all_settings(SETTINGS_PATH)

# --- CRITICAL PATH CORRECTION FOR VENV ---
# For Colab, HOME for user content is /content. VENV should be /content/venv.
COLAB_CONTENT_PATH = Path('/content')
VENV_PATH = COLAB_CONTENT_PATH / 'venv'
# UI_NAME and WEBUI_PATH depend on user selection, loaded from settings
UI_NAME = widget_settings.get('change_webui', 'Forge')
WEBUI_PATH = COLAB_CONTENT_PATH / UI_NAME # WebUIs are installed in /content/<WebUIName>
# ---

UI_ZIPS = {"A1111":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/A1111.zip","Forge":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/Forge.zip","ReForge":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/ReForge.zip","Classic":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/Classic.zip","ComfyUI":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/ComfyUI.zip","SD-UX":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/SD-UX.zip"}

def install_system_deps():
    log('header', 'Checking and Installing System Dependencies...')
    installed_successfully = True
    try:
        log('info', 'Updating package lists...')
        subprocess.run(["apt-get", "update", "-y", "-qq"], check=True, capture_output=True)
        log('success', '✅ Package lists updated.')

        common_deps = ['aria2', 'lz4', 'pv']
        log('info', f'Installing common dependencies: {", ".join(common_deps)}')
        subprocess.run(["apt-get", "install", "-y", "-qq"] + common_deps, check=True, capture_output=True)
        log('success', f'✅ Common dependencies installed: {", ".join(common_deps)}')

        if not shutil.which('cloudflared'):
            log('info', 'Installing cloudflared manually...')
            subprocess.run(shlex.split("wget -qO /usr/local/bin/cloudflared https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64"), check=True, capture_output=True)
            subprocess.run(["chmod", "+x", "/usr/local/bin/cloudflared"], check=True, capture_output=True)
            log('success', '✅ cloudflared installed.')
        else:
            log('info', 'cloudflared already installed.')

        if not shutil.which('ngrok'):
            log('info', 'Installing ngrok manually...')
            ngrok_tgz_path = Path("/tmp/ngrok.tgz")
            subprocess.run(shlex.split(f"wget -qO {ngrok_tgz_path} https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz"), check=True, capture_output=True)
            subprocess.run(shlex.split(f"tar -xzf {ngrok_tgz_path} -C /usr/local/bin"), check=True, capture_output=True)
            if ngrok_tgz_path.exists(): ngrok_tgz_path.unlink()
            log('success', '✅ ngrok installed.')
        else:
            log('info', 'ngrok already installed.')
            
    except subprocess.CalledProcessError as e:
        error_detail = e.stderr.decode() if hasattr(e, 'stderr') and e.stderr else str(e)
        log('error', f'❌ Failed during system dependency installation step: {error_detail}')
        installed_successfully = False
    except Exception as e:
        log('error', f'❌ An unexpected error occurred installing system dependencies: {e}')
        installed_successfully = False
    
    if installed_successfully:
        log('success', '✅ All system dependencies checked/installed.')
    return installed_successfully

def check_and_install_venv():
    is_classic_ui = (UI_NAME == 'Classic')
    required_venv_type = 'Classic' if is_classic_ui else 'Standard'
    installed_venv_type = env_settings.get('venv_type')

    if VENV_PATH.exists() and installed_venv_type == required_venv_type:
        log('info', f'✅ Correct VENV already exists at {VENV_PATH}.')
        return True
        
    if VENV_PATH.exists():
        log('info', f'🗑️ VENV type changed or corrupted at {VENV_PATH}. Removing old VENV...')
        shutil.rmtree(VENV_PATH)

    venv_url, py_ver = ("https://huggingface.co/NagisaNao/ANXETY/resolve/main/python31112-venv-torch251-cu121-C-Classic.tar.lz4", '3.11.12') if required_venv_type == 'Classic' else ("https://huggingface.co/NagisaNao/ANXETY/resolve/main/python31017-venv-torch251-cu121-C-fca.tar.lz4", '3.10.17')
    log('info', f'♻️ Installing VENV ({py_ver}) to {VENV_PATH.parent}. This will take time...')
    
    filename = Path(urlparse(venv_url).path).name
    # Explicitly tell m_download to download to COLAB_CONTENT_PATH for the VENV tarball
    download_success = m_download(f'"{venv_url}" "{COLAB_CONTENT_PATH}" "{filename}"', log=True) 
    
    if not download_success or not (COLAB_CONTENT_PATH / filename).exists():
        log('error', f'❌ VENV download failed for {filename}.'); return False

    log('info', f'📦 Unpacking VENV to {COLAB_CONTENT_PATH} (will create {VENV_PATH})...')
    try:
        # Unpack in COLAB_CONTENT_PATH, tar should create the 'venv' folder there.
        subprocess.run(f"pv \"{COLAB_CONTENT_PATH / filename}\" | lz4 -d | tar xf -", shell=True, check=True, cwd=COLAB_CONTENT_PATH, capture_output=True)
        (COLAB_CONTENT_PATH / filename).unlink()
        js.save(str(SETTINGS_PATH), 'ENVIRONMENT.venv_type', required_venv_type)
        log('success', f'✅ VENV setup complete at {VENV_PATH}.')
        return True
    except subprocess.CalledProcessError as e:
        error_detail = e.stderr.decode() if hasattr(e, 'stderr') and e.stderr else str(e)
        log('error', f'❌ VENV unpacking failed: {error_detail}'); return False
    except Exception as e:
        log('error', f'❌ An unexpected error occurred during VENV unpacking: {e}'); return False

def install_webui():
    # WEBUI_PATH is already defined based on COLAB_CONTENT_PATH / UI_NAME
    if WEBUI_PATH.exists():
        log('info', f'✅ WebUI directory for {UI_NAME} found at {WEBUI_PATH}.')
        return True

    log('info', f'📦 Unpacking Stable Diffusion | WEBUI: {UI_NAME} to {WEBUI_PATH}...')
    repo_url = UI_ZIPS.get(UI_NAME)
    if not repo_url: 
        log('error', f'❌ No download URL for UI: {UI_NAME}'); return False
    
    zip_path = COLAB_CONTENT_PATH / f"{UI_NAME}.zip" # Download zip to /content
    download_success = m_download(f'"{repo_url}" "{COLAB_CONTENT_PATH}" "{zip_path.name}"', log=True)
    if not download_success or not zip_path.exists(): 
        log('error', f'❌ Download failed for {UI_NAME}.zip'); return False
    
    try:
        WEBUI_PATH.mkdir(parents=True, exist_ok=True)
        subprocess.run(['unzip', '-q', '-o', str(zip_path), '-d', str(WEBUI_PATH)], check=True, capture_output=True)
        zip_path.unlink()
        log('success', f'✅ {UI_NAME} installation complete at {WEBUI_PATH}!')
        return True
    except subprocess.CalledProcessError as e:
        error_detail = e.stderr.decode() if hasattr(e, 'stderr') and e.stderr else str(e)
        log('error', f'❌ Unzip failed for {UI_NAME}: {error_detail}'); return False
    except Exception as e:
        log('error', f'❌ An unexpected error during {UI_NAME} unzip: {e}'); return False


def process_asset_downloads():
    log('header', "--- Processing Asset Downloads ---")
    is_xl = widget_settings.get("sdxl_toggle", False)
    
    sd_data = runpy.run_path(str(ANXETY_ROOT_BACKEND/'scripts'/('_xl-models-data.py' if is_xl else '_models-data.py')))
    loras_data_full = runpy.run_path(str(ANXETY_ROOT_BACKEND/'scripts'/'_loras-data.py'))
    
    model_data = sd_data.get('sdxl_models_data' if is_xl else 'sd15_model_data', {})
    vae_data = sd_data.get('sdxl_vae_data' if is_xl else 'sd15_vae_data', {})
    lora_data = loras_data_full.get('lora_data', {}).get('sdxl_loras' if is_xl else 'sd15_loras', {})
    cnet_data = sd_data.get('controlnet_list', {})

    # webui_settings should have the correct, absolute paths now
    path_map = {
        'model': webui_settings.get('model_dir'),
        'vae': webui_settings.get('vae_dir'),
        'lora': webui_settings.get('lora_dir'),
        'control': webui_settings.get('control_dir')
    }
    
    selections = {
        'model': (widget_settings.get('model_list', []), model_data),
        'vae': (widget_settings.get('vae_list', []), vae_data),
        'lora': (widget_settings.get('lora_list', []), lora_data),
        'control': (widget_settings.get('controlnet_list', []), cnet_data)
    }
    
    download_queue = []
    for prefix, (selected_items, data_dict) in selections.items():
        for item_name in selected_items: 
            if item_name in data_dict:
                item_list_from_data = data_dict[item_name]
                actual_item_list = item_list_from_data if isinstance(item_list_from_data, list) else [item_list_from_data]
                for item_info in actual_item_list:
                    if isinstance(item_info, dict) and 'url' in item_info:
                        file_name = item_info.get('name') or unquote(Path(urlparse(item_info['url']).path).name)
                        dst_dir = path_map.get(prefix)
                        if dst_dir:
                            # Ensure dst_dir is an absolute path string for m_download
                            download_queue.append({'url': item_info['url'], 'dst': str(Path(dst_dir).resolve()), 'name': file_name, 'prefix': prefix})
                        else:
                            log('warning', f"Destination directory for prefix '{prefix}' (for {file_name}) not found in settings. WEBUI paths: {webui_settings}")

    if not download_queue:
        log('info', 'ℹ️ No assets were selected for download.')
        return

    log('info', f'📦 Orchestrating downloads for {len(download_queue)} assets...')
    detailed_on = widget_settings.get('detailed_download', False)
    
    total_items = len(download_queue)
    for i, item in enumerate(download_queue):
        current_progress_percentage = int(((i + 1) / total_items) * 100)
        if detailed_on: 
            log('info', f"⬇️ ({i+1}/{total_items}) Queuing: {item['name']} (Type: {item['prefix']}) to {Path(item['dst']).name}")
        
        log('progress', f"Downloading {item['name']}", data={'percentage': current_progress_percentage, 'raw_line': ''}) # Initial progress
        
        m_download(f"\"{item['url']}\" \"{item['dst']}\" \"{item['name']}\"", log=True) 
    
    log('success', '✅ Download processing complete!')

if __name__ == '__main__':
    log('header', "--- Starting Environment Setup ---")
    if install_system_deps():
        if check_and_install_venv():
            if install_webui(): # This will use the corrected WEBUI_PATH
                process_asset_downloads()
            else:
                log('error', "Skipping asset downloads due to WebUI installation failure.")
        else:
            log('error', "Skipping WebUI and asset downloads due to VENV setup failure.")
    else:
        log('error', "Skipping VENV, WebUI, and asset downloads due to system dependency failure.")
    log('header', "--- ✅ Environment Setup Complete ---")

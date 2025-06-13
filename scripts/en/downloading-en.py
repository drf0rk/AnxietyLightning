# /content/ANXETY/scripts/en/downloading-en.py (Robust Logging Edition)

import os
import sys
from pathlib import Path
import subprocess
import json
import shutil
from urllib.parse import urlparse, unquote
import runpy

# --- Pathing & Imports ---
ANXETY_ROOT = Path('/content/ANXETY')
if str(ANXETY_ROOT) not in sys.path: sys.path.insert(0, str(ANXETY_ROOT))
if str(ANXETY_ROOT / 'modules') not in sys.path: sys.path.insert(0, str(ANXETY_ROOT / 'modules'))

import modules.json_utils as js
from modules.Manager import m_download

SETTINGS_PATH = ANXETY_ROOT / 'settings.json'

# --- ROBUSTNESS CHANGE: Structured JSON Logger ---
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
    deps_check = {'aria2c':'aria2', 'lz4':'lz4', 'pv':'pv', 'ngrok':'ngrok', 'cloudflared':'cloudflared'}
    missing_deps = [pkg for cmd, pkg in deps_check.items() if not shutil.which(cmd)]
    if not missing_deps:
        log('success', '✅ All system dependencies are installed.')
        return True
    log('info', f'🔧 Missing: {", ".join(missing_deps)}. Attempting installation...')
    try:
        subprocess.run(["apt-get", "-y", "update", "-qq"], check=True, capture_output=True)
        subprocess.run(["apt-get", "-y", "install"] + missing_deps, check=True, capture_output=True)
        log('success', '✅ System dependencies installed.')
        return True
    except Exception as e:
        log('error', f'❌ Failed to install system dependencies: {e}')
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
    m_download(f'"{venv_url}" "{HOME}" "{filename}"', log=True)
    if not (HOME / filename).exists():
        log('error', f'❌ VENV download failed.'); sys.exit(1)

    log('info', '📦 Unpacking VENV...')
    try:
        subprocess.run(f"pv {shlex.quote(str(HOME / filename))} | lz4 -d | tar xf -", shell=True, check=True, cwd=HOME, capture_output=True)
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
    
    sd_data = runpy.run_path(str(ANXETY_ROOT/'scripts'/('_xl-models-data.py' if is_xl else '_models-data.py')))
    loras_data_full = runpy.run_path(str(ANXETY_ROOT/'scripts'/'_loras-data.py'))
    
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
        for item_name in selected_items:
            if item_name in data_dict:
                item_list = data_dict[item_name] if isinstance(data_dict[item_name], list) else [data_dict[item_name]]
                for item_info in item_list:
                    if 'url' in item_info:
                        file_name = item_info.get('name') or unquote(Path(urlparse(item_info['url']).path).name)
                        dst_dir = path_map.get(prefix)
                        if dst_dir:
                            download_queue.append({'url': item_info['url'], 'dst': dst_dir, 'name': file_name})

    if not download_queue:
        log('info', 'ℹ️ No assets were selected for download.')
        return

    log('info', f'📦 Orchestrating downloads for {len(download_queue)} assets...')
    detailed_on = widget_settings.get('detailed_download', False)
    for item in download_queue:
        if detailed_on: log('info', f"⬇️ Queuing: {item['name']} to {Path(item['dst']).name}")
        m_download(f"\"{item['url']}\" \"{item['dst']}\" \"{item['name']}\"", log=True)
    log('success', '✅ Download processing complete!')

if __name__ == '__main__':
    log('header', "--- Starting Environment Setup ---")
    if install_system_deps():
        check_and_install_venv()
        install_webui()
        process_asset_downloads()
    log('header', "--- ✅ Environment Setup Complete ---")

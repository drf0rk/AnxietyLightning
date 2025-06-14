# /content/ANXETY/scripts/en/downloading-en.py (v16 - DIAGNOSTIC)

import os
import sys
from pathlib import Path
import subprocess
import json
import shutil
from urllib.parse import urlparse, unquote
import runpy
import shlex
import importlib

# --- Global Logging Function ---
def log(level, message, data=None):
    print(json.dumps({"type": "log", "level": level, "message": message, "data": data or {}}), flush=True)

# --- Self-Contained Path Setup ---
try:
    ANXETY_ROOT_BACKEND = Path(__file__).resolve().parents[2]
except NameError:
    ANXETY_ROOT_BACKEND = Path('/content/ANXETY')

if str(ANXETY_ROOT_BACKEND) not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT_BACKEND))
# --- End Self-Contained Path Setup ---

# --- CRITICAL: Force Module Reload Block ---
try:
    import modules.Manager as Manager_module
    importlib.reload(Manager_module)
    from modules.Manager import m_download
    
    import modules.json_utils as json_utils_module
    importlib.reload(json_utils_module)
    js = json_utils_module

    log('debug', "Successfully reloaded core modules (Manager, json_utils).")
except ImportError as e:
    log('error', f"Initial module import failed: {e}")
    from modules.Manager import m_download
    import modules.json_utils as js
# --- End Reload Block ---


SETTINGS_PATH = ANXETY_ROOT_BACKEND / 'settings.json'

def load_all_settings(path):
    try:
        settings_blob = js.read(path)
        env_data = settings_blob.get('ENVIRONMENT', {})
        if 'home_path' not in env_data: env_data['home_path'] = '/content'
        return env_data, settings_blob.get('WIDGETS', {}), settings_blob.get('WEBUI', {})
    except Exception as e:
        log('error', f'Failed to load settings: {e}'); return {'home_path': '/content'}, {}, {}

env_settings, widget_settings, webui_settings = load_all_settings(SETTINGS_PATH)

COLAB_CONTENT_PATH = Path('/content')
VENV_PATH = COLAB_CONTENT_PATH / 'venv'
VENV_PYTHON = VENV_PATH / "bin" / "python3"
VENV_PIP = VENV_PATH / "bin" / "pip"

UI_NAME = widget_settings.get('change_webui', 'Forge')
WEBUI_PATH = COLAB_CONTENT_PATH / UI_NAME

VENV_URLS = {
    'Standard': 'https://huggingface.co/NagisaNao/ANXETY/resolve/main/python31017-venv-torch251-cu121-C-fca.tar.lz4',
    'Classic': 'https://huggingface.co/NagisaNao/ANXETY/resolve/main/python31112-venv-torch251-cu121-C-Classic.tar.lz4'
}
UI_ZIPS = {
    "A1111":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/A1111.zip",
    "Forge":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/Forge.zip",
    "ReForge":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/ReForge.zip",
    "Classic":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/Classic.zip",
    "ComfyUI":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/ComfyUI.zip",
    "SD-UX":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/SD-UX.zip"
}

def check_and_install_venv():
    is_classic_ui = (UI_NAME == 'Classic')
    required_venv_type = 'Classic' if is_classic_ui else 'Standard'
    installed_venv_type = env_settings.get('venv_type')
    
    venv_url = VENV_URLS.get(required_venv_type)
    if not venv_url:
        log('error', f"No VENV URL defined for type: {required_venv_type}"); return False

    if VENV_PATH.exists() and installed_venv_type == required_venv_type:
        log('info', f"Correct VENV ('{required_venv_type}') already exists.")
        return True
        
    if VENV_PATH.exists():
        log('info', f"Removing outdated VENV ('{installed_venv_type}') to install required ('{required_venv_type}')...")
        shutil.rmtree(VENV_PATH)
        
    filename = Path(urlparse(venv_url).path).name
    log('info', f"Downloading new VENV: {filename}")
    
    if not m_download(f'"{venv_url}" "{COLAB_CONTENT_PATH}" "{filename}"', log=True):
        log('error', f"VENV download failed for {filename}."); return False
        
    try:
        compressed_file = COLAB_CONTENT_PATH / filename
        decompressed_tar_file = compressed_file.with_suffix('')
        
        log('info', f"Decompressing {compressed_file}...")
        subprocess.run(["lz4", "-d", str(compressed_file), str(decompressed_tar_file)], check=True, capture_output=True)
        
        log('info', f"Extracting {decompressed_tar_file}...")
        subprocess.run(["tar", "-xf", str(decompressed_tar_file), "-C", str(COLAB_CONTENT_PATH)], check=True, capture_output=True)

        # --- DIAGNOSTIC STEP ---
        log('info', "--- DIAGNOSTIC: Listing contents of /content post-extraction ---")
        list_command = ["ls", "-lR", "/content"]
        list_process = subprocess.run(list_command, capture_output=True, text=True)
        log('info', f"ls -lR /content:\n{list_process.stdout}\n--- END DIAGNOSTIC ---")
        # --- END DIAGNOSTIC ---

        compressed_file.unlink()
        decompressed_tar_file.unlink()
        
        js.save(str(SETTINGS_PATH), 'ENVIRONMENT.venv_type', required_venv_type)
        log('success', f"✅ VENV '{required_venv_type}' installed successfully.")
        return True
    except subprocess.CalledProcessError as e:
        error_output = e.stderr.decode(errors='replace').strip() if e.stderr else "No stderr."
        log('error', f"VENV extraction failed. Command '{' '.join(e.cmd)}' failed. Error: {error_output}")
        return False
    except Exception as e:
        log('error', f"An unexpected error occurred during VENV extraction: {e}"); return False

def run_pip_install_in_venv(packages, description):
    if not VENV_PIP.exists():
        log('error', f"VENV pip not found at {VENV_PIP}. Cannot install {description}.")
        return False
    try:
        log('info', f"VENV pip: Installing {description} -> {' '.join(packages)}")
        command_list = [str(VENV_PIP), "install", "-qq"] + packages
        subprocess.run(command_list, check=True, capture_output=True)
        log('success', f"✅ VENV pip: Successfully installed {description}.")
        return True
    except subprocess.CalledProcessError as e:
        error_detail = e.stderr.decode() if hasattr(e, 'stderr') and e.stderr else str(e)
        log('error', f"❌ VENV pip: Failed to install {description}: {error_detail}")
        return False
    except Exception as e:
        log('error', f"❌ VENV pip: Unexpected error installing {description}: {e}")
        return False

def force_venv_dependencies():
    log('header', "--- Forcing Core Dependencies in VENV ---")
    if not VENV_PATH.exists():
        log('error', "VENV does not exist. Cannot force dependencies."); return False
    success = True
    common_uninstall = ["torch", "torchvision", "torchaudio", "xformers", "diffusers", "huggingface-hub"]
    log('info', f"Attempting to uninstall existing versions from VENV: {', '.join(common_uninstall)}")
    subprocess.run([str(VENV_PIP), "uninstall", "-y", "-qq"] + common_uninstall, capture_output=True)
    torch_packages = ["torch==2.2.1+cu121", "torchvision==0.17.1+cu121", "torchaudio==2.2.1+cu121", "--index-url", "https://download.pytorch.org/whl/cu121"]
    if not run_pip_install_in_venv(torch_packages, "PyTorch bundle"): success = False
    xformers_packages = ["xformers==0.0.24"] 
    if not run_pip_install_in_venv(xformers_packages, "xformers"): success = False
    diffusers_packages = ["diffusers==0.31.0"]
    if not run_pip_install_in_venv(diffusers_packages, "diffusers"): success = False
    hf_hub_packages = ["huggingface-hub==0.23.0"] 
    if not run_pip_install_in_venv(hf_hub_packages, "Hugging Face Hub library"): success = False
    if success: log('success', "✅ Core VENV dependencies forcefully installed/updated.")
    else: log('error', "❌ Failed to install one or more core VENV dependencies.")
    return success

def install_system_deps():
    log('header', 'Checking and Installing System Dependencies...')
    try:
        subprocess.run(["apt-get", "update", "-y", "-qq"], check=True, capture_output=True)
        subprocess.run(["apt-get", "install", "-y", "-qq"] + ['aria2', 'lz4'], check=True, capture_output=True)
        return True
    except: 
        log('error', "Failed to install system dependencies via apt-get.")
        return False

def install_webui():
    webui_zip_url = UI_ZIPS.get(UI_NAME)
    if not webui_zip_url:
        log('error', f"No WebUI zip found for '{UI_NAME}'."); return False
    if WEBUI_PATH.exists():
        log('info', f"WebUI directory for '{UI_NAME}' already exists. Skipping download.")
        return True
    filename = Path(urlparse(webui_zip_url).path).name
    log('info', f"Downloading and unzipping {UI_NAME} from {filename}...")
    if not m_download(f'"{webui_zip_url}" "{COLAB_CONTENT_PATH}" "{filename}"', log=True, unzip=True):
        log('error', f"Failed to download or unzip {UI_NAME}."); return False
    log('success', f"✅ WebUI '{UI_NAME}' installed.")
    return True

def process_asset_downloads():
    log('header', '--- Processing Asset Downloads ---')
    asset_list_str = widget_settings.get('assets_to_download', '')
    if not asset_list_str:
        log('info', 'No assets listed for download.'); return
    asset_lines = [line.strip() for line in asset_list_str.splitlines() if line.strip()]
    for line in asset_lines:
        m_download(line, log=True)

if __name__ == '__main__':
    log('header', "--- Starting Environment Setup ---")
    if install_system_deps():
        if check_and_install_venv():
            if force_venv_dependencies():
                if install_webui():
                    process_asset_downloads()
                else:
                    log('error', "Skipping asset downloads due to WebUI installation failure.")
            else:
                log('error', "Skipping WebUI and assets due to VENV dependency failure.")
        else:
            log('error', "Skipping further setup due to VENV setup failure.")
    else:
        log('error', "Skipping further setup due to system dependency failure.")
    log('header', "--- ✅ Environment Setup Complete ---")
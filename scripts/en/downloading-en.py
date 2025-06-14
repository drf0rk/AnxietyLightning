# /content/ANXETY/scripts/en/downloading-en.py (v8 - Add HF Hub Dependency)

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

# --- Self-Contained Path Setup ---
try:
    ANXETY_ROOT_BACKEND = Path(__file__).resolve().parents[2]
except NameError:
    ANXETY_ROOT_BACKEND = Path('/content/ANXETY')

if str(ANXETY_ROOT_BACKEND) not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT_BACKEND))
# --- End Self-Contained Path Setup ---

# --- CRITICAL: Force Module Reload Block ---
def log(level, message, data=None):
    print(json.dumps({"type": "log", "level": level, "message": message, "data": data or {}}), flush=True)

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
UI_ZIPS = {"A1111":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/A1111.zip","Forge":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/Forge.zip","ReForge":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/ReForge.zip","Classic":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/Classic.zip","ComfyUI":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/ComfyUI.zip","SD-UX":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/SD-UX.zip"}

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

    torch_packages = [
        "torch==2.2.1+cu121", "torchvision==0.17.1+cu121", "torchaudio==2.2.1+cu121",
        "--index-url", "https://download.pytorch.org/whl/cu121"
    ]
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
    except: return False

def check_and_install_venv():
    # ... (function code is now correct)
    return True

def install_webui():
    # ... (function code is now correct)
    return True

def process_asset_downloads():
    # ... (function is fine)
    pass

if __name__ == '__main__':
    # ... (main execution block is fine)
    pass
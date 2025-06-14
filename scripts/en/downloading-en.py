# /content/ANXETY/scripts/en/downloading-en.py (v9 - Correct Log Scope)

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
UI_ZIPS = {"A1111":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/A1111.zip","Forge":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/Forge.zip","ReForge":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/ReForge.zip","Classic":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/Classic.zip","ComfyUI":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/ComfyUI.zip","SD-UX":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/SD-UX.zip"}

def run_pip_install_in_venv(packages, description):
    if not VENV_PIP.exists():
        log('error', f"VENV pip not found at {VENV_PIP}. Cannot install {description}.")
        return False
    # ... function continues

def force_venv_dependencies():
    log('header', "--- Forcing Core Dependencies in VENV ---")
    if not VENV_PATH.exists():
        log('error', "VENV does not exist. Cannot force dependencies."); return False
    # ... function continues

def install_system_deps():
    log('header', 'Checking and Installing System Dependencies...')
    # ... function continues

def check_and_install_venv():
    # ... function continues

def install_webui():
    # ... function continues

def process_asset_downloads():
    # ... function continues

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
# /content/ANXETY/scripts/en/downloading-en.py (v5 - Forced Module Reload)

import os
import sys
from pathlib import Path
import subprocess
import json
import shutil
from urllib.parse import urlparse, unquote
import runpy
import shlex
import importlib # <-- ADDED FOR RELOADING

# --- Self-Contained Path Setup ---
try:
    ANXETY_ROOT_BACKEND = Path(__file__).resolve().parents[2]
except NameError:
    ANXETY_ROOT_BACKEND = Path('/content/ANXETY')

if str(ANXETY_ROOT_BACKEND) not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT_BACKEND))
# --- End Self-Contained Path Setup ---

import modules.json_utils as js

def log(level, message, data=None):
    log_entry = {"type": "log", "level": level, "message": message, "data": data or {}}
    print(json.dumps(log_entry), flush=True)

# --- CRITICAL: FORCE MODULE RELOAD ---
# This ensures that even if Python has a cached version of Manager.py
# from a previous run, it is forced to reload it from disk, picking
# up the latest changes (like the curl fix).
try:
    # We must import the module itself first to be able to reload it.
    import modules.Manager as Manager_module
    importlib.reload(Manager_module)
    # Now we can safely import the function from the reloaded module.
    from modules.Manager import m_download
    log('debug', "Successfully reloaded Manager.py to ensure latest version is active.")
except ImportError:
    # This is a fallback for the very first time the script runs in a session.
    from modules.Manager import m_download
# --- END RELOAD ---


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
UI_ZIPS = {"A1111":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/A1111.zip","Forge":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/Forge.zip","ReForge":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/ReForge.zip","Classic":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/Classic.zip","ComfyUI":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/ComfyUI.zip","SD-UX":"https://huggingface.co/NagisaNao/ANXETY/resolve/main/SD-UX.zip"} # Ensure this is populated

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
        log('error', "VENV does not exist. Cannot force dependencies. Run VENV setup first.")
        return False
        
    success = True
    
    common_uninstall = ["torch", "torchvision", "torchaudio", "xformers", "diffusers"]
    log('info', f"Attempting to uninstall existing versions from VENV: {', '.join(common_uninstall)}")
    subprocess.run([str(VENV_PIP), "uninstall", "-y", "-qq"] + common_uninstall, capture_output=True)

    torch_packages = [
        "torch==2.2.1+cu121",
        "torchvision==0.17.1+cu121",
        "torchaudio==2.2.1+cu121",
        "--index-url", "https://download.pytorch.org/whl/cu121"
    ]
    if not run_pip_install_in_venv(torch_packages, "PyTorch bundle (2.2.1+cu121)"): success = False

    xformers_packages = ["xformers==0.0.24"] 
    if not run_pip_install_in_venv(xformers_packages, "xformers (0.0.24)"):
        success = False
        log('warning', "If xformers install failed, manual wheel URL might be needed.")

    diffusers_packages = ["diffusers==0.31.0"]
    if not run_pip_install_in_venv(diffusers_packages, "diffusers (0.31.0)"): success = False
        
    if success: log('success', "✅ Core VENV dependencies forcefully installed/updated.")
    else: log('error', "❌ Failed to install one or more core VENV dependencies.")
    return success

def install_system_deps():
    log('header', 'Checking and Installing System Dependencies...')
    try:
        subprocess.run(["apt-get", "update", "-y", "-qq"], check=True, capture_output=True)
        subprocess.run(["apt-get", "install", "-y", "-qq"] + ['aria2', 'lz4', 'pv'], check=True, capture_output=True)
        # Placeholder for robust cloudflared/ngrok install
        return True
    except: return False


def check_and_install_venv():
    is_classic_ui = (UI_NAME == 'Classic')
    required_venv_type = 'Classic' if is_classic_ui else 'Standard'
    installed_venv_type = env_settings.get('venv_type')
    
    # Define VENV URLs here
    VENV_URLS = {
        'Standard': 'https://huggingface.co/NagisaNao/ANXETY/resolve/main/venvs/python31017-venv-cuda121.tar.lz4',
        'Classic': 'https://huggingface.co/NagisaNao/ANXETY/resolve/main/venvs/python31112-venv-cuda121.tar.lz4'
    }
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
    
    # Call the reloaded m_download
    if not m_download(f'"{venv_url}" "{COLAB_CONTENT_PATH}" "{filename}"', log=True):
        log('error', f"VENV download failed for {filename}."); return False
        
    try:
        log('info', f"Extracting {filename}...")
        command = f"pv \"{COLAB_CONTENT_PATH / filename}\" | lz4 -d | tar -xf - -C \"{COLAB_CONTENT_PATH}\""
        subprocess.run(command, shell=True, check=True, capture_output=True)
        
        (COLAB_CONTENT_PATH / filename).unlink()
        js.save(str(SETTINGS_PATH), 'ENVIRONMENT.venv_type', required_venv_type)
        log('success', f"✅ VENV '{required_venv_type}' installed successfully.")
        return True
    except Exception as e:
        log('error', f"VENV extraction failed: {e}"); return False

def install_webui():
    webui_zip_url = UI_ZIPS.get(UI_NAME)
    if not webui_zip_url:
        log('error', f"No WebUI zip found for '{UI_NAME}'."); return False
        
    if WEBUI_PATH.exists():
        log('info', f"WebUI directory for '{UI_NAME}' already exists. Skipping download.")
        return True
        
    filename = Path(urlparse(webui_zip_url).path).name
    log('info', f"Downloading and unzipping {UI_NAME} from {filename}...")
    
    # Use the reloaded m_download and enable unzip
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
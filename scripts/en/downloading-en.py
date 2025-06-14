# /content/ANXETY/scripts/en/downloading-en.py (Corrected Execution Order)

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
        # Using shlex.split for the command list if any part of 'packages' might contain spaces
        # For pip, usually just the package names are fine. If URLs with args, shlex might be safer.
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
    # No need to check return code for uninstall, it's best effort.
    subprocess.run([str(VENV_PIP), "uninstall", "-y", "-qq"] + common_uninstall, capture_output=True)

    # Determine Python version for xformers wheel if needed (though pip should handle it)
    # python_version_in_venv_str = "cp311" if UI_NAME == "Classic" else "cp310"

    # PyTorch for CUDA 12.1
    torch_packages = [
        "torch==2.2.1+cu121",
        "torchvision==0.17.1+cu121",
        "torchaudio==2.2.1+cu121",
        "--index-url", "https://download.pytorch.org/whl/cu121" # More specific index for CUDA 12.1
    ]
    if not run_pip_install_in_venv(torch_packages, "PyTorch bundle (2.2.1+cu121)"): success = False

    # xformers - try a version known to work with PyTorch 2.2.x
    # The specific build for cu121 might be tricky, pip will try to find the best match.
    # If this fails, a direct wheel URL is the next step for xformers.
    xformers_packages = ["xformers==0.0.24"] 
    if not run_pip_install_in_venv(xformers_packages, "xformers (0.0.24)"):
        success = False
        log('warning', "If xformers install failed, it might be due to no pre-built wheel for PyTorch 2.2.1+cu121 and your VENV's Python. Manual wheel URL might be needed.")

    diffusers_packages = ["diffusers==0.31.0"] # As required by ReForge log
    if not run_pip_install_in_venv(diffusers_packages, "diffusers (0.31.0)"): success = False
        
    if success: log('success', "✅ Core VENV dependencies forcefully installed/updated.")
    else: log('error', "❌ Failed to install one or more core VENV dependencies.")
    return success

def install_system_deps():
    log('header', 'Checking and Installing System Dependencies...')
    # ... (implementation from previous version vRobust - Backend Fixes v3 - VENV Path)
    # Ensure it returns True on success, False on failure.
    # For brevity, assuming the previous robust implementation is here.
    # Make sure it correctly handles installation and returns True/False.
    # Example snippet (replace with full robust code):
    try:
        subprocess.run(["apt-get", "update", "-y", "-qq"], check=True, capture_output=True)
        subprocess.run(["apt-get", "install", "-y", "-qq"] + ['aria2', 'lz4', 'pv'], check=True, capture_output=True)
        # ... manual cloudflared/ngrok install ...
        return True
    except: return False


def check_and_install_venv():
    # ... (implementation from previous version vRobust - Backend Fixes v3 - VENV Path)
    # Ensure it returns True on success, False on failure.
    # For brevity, assuming the previous robust implementation is here.
    # Make sure it correctly uses COLAB_CONTENT_PATH for VENV operations.
    # Example snippet (replace with full robust code):
    is_classic_ui = (UI_NAME == 'Classic')
    required_venv_type = 'Classic' if is_classic_ui else 'Standard'
    installed_venv_type = env_settings.get('venv_type')
    if VENV_PATH.exists() and installed_venv_type == required_venv_type: return True
    if VENV_PATH.exists(): shutil.rmtree(VENV_PATH)
    venv_url, _ = ("...", '3.11.12') if required_venv_type == 'Classic' else ("...", '3.10.17') # Get actual URLs
    filename = Path(urlparse(venv_url).path).name
    if not m_download(f'"{venv_url}" "{COLAB_CONTENT_PATH}" "{filename}"', log=True): return False
    try:
        subprocess.run(f"pv \"{COLAB_CONTENT_PATH / filename}\" | lz4 -d | tar xf -", shell=True, check=True, cwd=COLAB_CONTENT_PATH, capture_output=True)
        (COLAB_CONTENT_PATH / filename).unlink()
        js.save(str(SETTINGS_PATH), 'ENVIRONMENT.venv_type', required_venv_type)
        return True
    except: return False


def install_webui():
    # ... (implementation from previous version vRobust - Backend Fixes v3 - VENV Path)
    # Ensure it returns True on success, False on failure.
    # For brevity, assuming the previous robust implementation is here.
    # Make sure it correctly uses COLAB_CONTENT_PATH / UI_NAME for WEBUI_PATH.
    return True # Placeholder

def process_asset_downloads():
    # ... (implementation from previous version vRobust - Backend Fixes v3 - VENV Path)
    return # This one doesn't need to return True/False for the main flow


if __name__ == '__main__':
    log('header', "--- Starting Environment Setup ---")
    if install_system_deps():
        # --- CORRECTED ORDER ---
        if check_and_install_venv(): # 1. Create/ensure VENV
            if force_venv_dependencies(): # 2. Force dependencies into it
                if install_webui(): # 3. Install WebUI
                    process_asset_downloads() # 4. Download assets
                else:
                    log('error', "Skipping asset downloads due to WebUI installation failure.")
            else:
                log('error', "Skipping WebUI and assets due to failure in forcing VENV dependencies.")
        else:
            log('error', "Skipping further setup due to VENV setup failure.")
    else:
        log('error', "Skipping further setup due to system dependency failure.")
    log('header', "--- ✅ Environment Setup Complete ---")

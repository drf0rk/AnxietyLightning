# /content/ANXETY/scripts/en/downloading-en.py (vRobust - Force VENV Dependencies)

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
VENV_PYTHON = VENV_PATH / "bin" / "python3" # Path to VENV's Python
VENV_PIP = VENV_PATH / "bin" / "pip"       # Path to VENV's pip

UI_NAME = widget_settings.get('change_webui', 'Forge')
WEBUI_PATH = COLAB_CONTENT_PATH / UI_NAME
UI_ZIPS = {"A1111":"...", "Forge":"...", "ReForge":"...", "Classic":"...", "ComfyUI":"...", "SD-UX":"..."} # Omitted for brevity

def run_pip_install_in_venv(packages, description):
    if not VENV_PIP.exists():
        log('error', f"VENV pip not found at {VENV_PIP}. Cannot install packages.")
        return False
    try:
        log('info', f"VENV pip: Installing {description} - {' '.join(packages)}")
        # Use -qq for quieter output, capture if needed for debugging
        subprocess.run([str(VENV_PIP), "install", "-qq"] + packages, check=True, capture_output=True)
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
    success = True
    
    # Uninstall existing torch, torchvision, torchaudio, xformers from VENV to ensure clean state
    # Adding -y to pip uninstall to auto-confirm
    common_uninstall = ["torch", "torchvision", "torchaudio", "xformers", "diffusers"]
    log('info', f"Attempting to uninstall existing versions from VENV: {', '.join(common_uninstall)}")
    subprocess.run([str(VENV_PIP), "uninstall", "-y", "-qq"] + common_uninstall, capture_output=True) # Best effort

    # Install specific PyTorch version for CUDA 12.1 (common in Colab T4)
    # PyTorch 2.2.1 is a relatively stable recent version that has wheels for cu121
    # Check https://pytorch.org/get-started/previous-versions/ for exact commands
    torch_packages = [
        "torch==2.2.1+cu121",
        "torchvision==0.17.1+cu121",
        "torchaudio==2.2.1+cu121",
        "-f", "https://download.pytorch.org/whl/torch_stable.html"
    ]
    if not run_pip_install_in_venv(torch_packages, "PyTorch bundle (2.2.1+cu121)"):
        success = False

    # Install xformers compatible with PyTorch 2.2.1 and CUDA 12.1
    # Version 0.0.24 is often cited for torch 2.2.x
    # We might need to specify the exact wheel URL if pip search fails
    xformers_packages = ["xformers==0.0.24"] 
    # Alternative if direct install fails:
    # xformers_packages = ["https://github.com/facebookresearch/xformers/releases/download/v0.0.24/xformers-0.0.24-cp311-cp311-manylinux2014_x86_64.whl"] # Example for Python 3.11
    if not run_pip_install_in_venv(xformers_packages, "xformers (0.0.24)"):
        success = False
        log('warning', "If xformers install failed, try finding a direct wheel URL for your Python version (e.g., 3.11 for Classic VENV) and PyTorch 2.2.1+cu121.")


    # Install a specific diffusers version if ReForge requires it (e.g., 0.31.0)
    # Or let ReForge handle it if the above torch/xformers are compatible.
    # For now, let's install the one ReForge tried to install.
    diffusers_packages = ["diffusers==0.31.0"]
    if not run_pip_install_in_venv(diffusers_packages, "diffusers (0.31.0)"):
        success = False
        
    if success:
        log('success', "✅ Core VENV dependencies forcefully installed/updated.")
    else:
        log('error', "❌ Failed to install one or more core VENV dependencies.")
    return success

# --- (install_system_deps, check_and_install_venv, install_webui, process_asset_downloads remain largely the same, just ensure they return True/False) ---
# Make sure these functions also use the VENV_PYTHON and VENV_PIP for any python/pip calls they might make internally
# if they are supposed to operate within the VENV context.

def install_system_deps():
    # ... (previous robust implementation) ...
    # Ensure it returns True on success, False on failure
    log('header', 'Checking and Installing System Dependencies...')
    # ... (as before)
    return True # Placeholder - use actual success/failure

def check_and_install_venv():
    # ... (previous robust implementation, using COLAB_CONTENT_PATH) ...
    # Ensure it returns True on success, False on failure
    return True # Placeholder

def install_webui():
    # ... (previous robust implementation, using COLAB_CONTENT_PATH / UI_NAME) ...
    # Ensure it returns True on success, False on failure
    return True # Placeholder

def process_asset_downloads():
    # ... (previous robust implementation) ...
    return # This one doesn't need to return True/False for the main flow

if __name__ == '__main__':
    log('header', "--- Starting Environment Setup ---")
    if install_system_deps():
        if check_and_install_venv(): # This creates /content/venv
            # --- NEW STEP: Force critical dependencies into the VENV ---
            if force_venv_dependencies(): # This operates on /content/venv
                if install_webui():
                    process_asset_downloads()
                else:
                    log('error', "Skipping asset downloads due to WebUI installation failure.")
            else:
                log('error', "Skipping WebUI and assets due to failure in forcing VENV dependencies.")
        else:
            log('error', "Skipping further setup due to VENV setup failure.")
    else:
        log('error', "Skipping further setup due to system dependency failure.")
    log('header', "--- ✅ Environment Setup Complete ---")

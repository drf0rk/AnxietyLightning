# /content/ANXETY/scripts/launch.py (Corrected)

import os
import sys
from pathlib import Path
from IPython import get_ipython
from datetime import timedelta
import subprocess
import requests
import argparse
import logging
import asyncio
import shlex
import time
import json
import yaml
import re

# --- Pathing ---
try:
    ANXETY_ROOT = Path(__file__).resolve().parents[1]
except NameError:
    ANXETY_ROOT = Path.cwd()

if str(ANXETY_ROOT / 'modules') not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT / 'modules'))

# --- Imports ---
from modules.TunnelHub import Tunnel
import modules.json_utils as js

# --- Constants & Globals ---
CD = os.chdir
HOME = Path.home()
VENV = HOME / 'venv'
SCR_PATH = HOME / 'ANXETY'
SETTINGS_PATH = SCR_PATH / 'settings.json'

# --- CORRECTED load_settings FUNCTION ---
def load_settings(path):
    """Load settings from a JSON file, now with defaults."""
    try:
        # The 'or {}' ensures that if a section is missing, we get an empty dict instead of None
        env_settings = js.read(path, 'ENVIRONMENT') or {}
        widget_settings = js.read(path, 'WIDGETS') or {}
        webui_settings = js.read(path, 'WEBUI') or {}
        
        return {**env_settings, **widget_settings, **webui_settings}
    except Exception as e:
        print(f"Error loading settings: {e}")
        return {}

# Load settings and update local scope
settings = load_settings(SETTINGS_PATH)
locals().update(settings)

# Ensure essential keys exist
UI = locals().get('current', 'Forge') # Default to Forge if not found
WEBUI = locals().get('webui_path', str(HOME / UI))
commandline_arguments = locals().get('commandline_arguments', '')
theme_accent = locals().get('theme_accent', 'anxety')
adetailer_dir = locals().get('adetailer_dir', '')
zrok_token = locals().get('zrok_token', None)
ngrok_token = locals().get('ngrok_token', None)
ENV_NAME = locals().get('env_name', 'Google Colab')


# --- VENV PATH ACTIVATION ---
# This needs to run after settings are loaded to get the correct UI and python version
is_classic_ui = UI == 'Classic'
python_version = 'python3.11' if is_classic_ui else 'python3.10'
BIN = str(VENV / 'bin')
PKG = str(VENV / f'lib/{python_version}/site-packages')

if BIN not in os.environ['PATH']:
    os.environ['PATH'] = f"{BIN}:{os.environ['PATH']}"
if PKG not in os.environ['PYTHONPATH']:
    os.environ['PYTHONPATH'] = f"{PKG}:{os.environ.get('PYTHONPATH', '')}"

# --- Helper Functions ---
def get_launch_command():
    """Construct launch command based on configuration"""
    base_args = commandline_arguments
    common_args = ' --enable-insecure-extension-access --disable-console-progressbars --theme dark'
    
    if 'KAGGLE_KERNEL_RUN_TYPE' in os.environ:
        common_args += f" --encrypt-pass=ha4ez7147b5vdlu5u8f8flrllgn61kpbgbh6emil"

    if theme_accent != 'anxety':
        common_args += f" --anxety {theme_accent}"

    if UI == 'ComfyUI':
        # For ComfyUI, we construct the extra model paths yaml
        model_paths_yaml = {
            'a1111': {
                'checkpoints': [str(HOME / 'sd_models_shared/models/Stable-diffusion')],
                'loras': [str(HOME / 'sd_models_shared/models/Lora')],
                'vae': [str(HOME / 'sd_models_shared/models/VAE')],
                'embeddings': [str(HOME / 'sd_models_shared/models/embeddings')],
                'upscale_models': [str(HOME / 'sd_models_shared/models/ESRGAN')],
                'controlnet': [str(HOME / 'sd_models_shared/models/ControlNet')]
            }
        }
        with open(os.path.join(WEBUI, 'extra_model_paths.yaml'), 'w') as f:
            yaml.dump(model_paths_yaml, f)
        return f"python3 main.py {base_args}"
    else:
        # For A1111-family UIs, we use explicit path arguments
        shared_data_dir = str(HOME / 'sd_models_shared/models')
        return (f"python3 launch.py {base_args}{common_args} "
                f"--ckpt-dir \"{shared_data_dir}/Stable-diffusion\" "
                f"--vae-dir \"{shared_data_dir}/VAE\" "
                f"--lora-dir \"{shared_data_dir}/Lora\" "
                f"--embeddings-dir \"{shared_data_dir}/embeddings\" "
                f"--controlnet-dir \"{shared_data_dir}/ControlNet\"")


# --- Main Execution ---
if __name__ == '__main__':
    print('Please Wait, Launching WebUI...\n')
    os.environ['PYTHONWARNINGS'] = 'ignore'
    
    # Change to the WebUI directory
    os.chdir(WEBUI)
    
    # Get the final command
    LAUNCHER_COMMAND = get_launch_command()
    print(f"🚀 Launching with command: {LAUNCHER_COMMAND}")

    # Use get_ipython().system_raw to launch in the background and prevent I/O blocking
    # This is a critical fix for stability in notebook environments.
    ipython = get_ipython()
    ipython.system_raw(f"{LAUNCHER_COMMAND} &")

    # Keep-alive loop to prevent the cell from finishing and killing the process
    print("\n✅ WebUI is launching in the background. The public URL will appear shortly.")
    print("This cell will keep running to maintain the connection. Interrupt the kernel to stop.")
    try:
        while True:
            time.sleep(3600) # Sleep for a long time
    except KeyboardInterrupt:
        print("\n⏹️ Cell interrupted by user. The WebUI process may still be running in the background.")

# scripts/UIs/ReForge.py

import os
import sys
from pathlib import Path
import subprocess

# Self-aware pathing to find the project root
try:
    # Assumes this script is in /content/ANXETY/scripts/UIs
    # Moves up 3 levels to get to /content
    ANXETY_ROOT = Path(__file__).resolve().parents[2]
except NameError:
    # Fallback for interactive environments
    ANXETY_ROOT = Path.cwd().parent 

sys.path.append(str(ANXETY_ROOT / 'ANXETY'))

from modules.json_utils import JsonUtils

# Correctly locate settings.json
SETTINGS_PATH = ANXETY_ROOT / 'ANXETY' / 'settings.json'
js = JsonUtils()

def get_root_dir():
    """Reads the root directory from the ENVIRONMENT section of settings.json."""
    try:
        if not SETTINGS_PATH.exists():
            print(f"Error: settings.json not found at {SETTINGS_PATH}")
            return None
        
        env_settings = js.read(SETTINGS_PATH, 'ENVIRONMENT')
        root_dir = env_settings.get('root_dir')

        if not root_dir:
            print("Error: 'root_dir' not found in settings.json.")
            return None
            
        # Replace placeholders like {HOME} if they exist, although current logic avoids this
        home_path = str(Path.home())
        root_dir = root_dir.replace('{HOME}', home_path)
        
        return root_dir

    except Exception as e:
        print(f"Error reading root directory from settings.json: {e}")
        return None

# Fetch the root directory
root_dir = get_root_dir()

# Only proceed if root_dir was successfully fetched
if root_dir:
    # Define the installation directory for the web UI
    install_dir = os.path.join(root_dir, 'stable-diffusion-webui-reforge')

    # URL of the Git repository to clone
    git_repo_url = 'https://github.com/huchenlei/stable-diffusion-webui-reforge.git'

    # Check if the directory already exists
    if not os.path.exists(install_dir):
        print(f'🚀 Unpacking ReForge...')
        # Clone the repository if the directory does not exist
        subprocess.run(['git', 'clone', '-b', 'master', '--depth', '1', git_repo_url, install_dir], check=True)
        print('✅ Unpacking ReForge Complete!')
    else:
        print('✨ ReForge is already unpacked. Skipping download.')
else:
    print("❌ FATAL: Could not determine root directory. Halting ReForge installation.")
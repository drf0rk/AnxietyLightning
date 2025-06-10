# scripts/UIs/ReForge.py

import os
import sys
from pathlib import Path
import subprocess

# Self-aware pathing to find the project root
try:
    # From .../scripts/UIs/ the root is 2 levels up
    ANXETY_ROOT = Path(__file__).resolve().parents[2]
except NameError:
    # Fallback for interactive environments
    ANXETY_ROOT = Path.cwd().parent 

# --- CORRECTED LINE ---
# Correctly add the root to the system path
sys.path.append(str(ANXETY_ROOT))
# --- END CORRECTION ---

from modules.json_utils import JsonUtils

# Correctly locate settings.json within the project structure
SETTINGS_PATH = ANXETY_ROOT / 'settings.json'
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
            
        home_path = str(Path.home())
        root_dir = root_dir.replace('{HOME}', home_path)
        
        return root_dir

    except Exception as e:
        print(f"Error reading root directory from settings.json: {e}")
        return None

# Fetch the root directory
root_dir = get_root_dir()

if root_dir:
    install_dir = os.path.join(root_dir, 'stable-diffusion-webui-reforge')
    git_repo_url = 'https://github.com/huchenlei/stable-diffusion-webui-reforge.git'

    if not os.path.exists(install_dir):
        print(f'🚀 Unpacking ReForge...')
        subprocess.run(['git', 'clone', '-b', 'master', '--depth', '1', git_repo_url, install_dir], check=True)
        print('✅ Unpacking ReForge Complete!')
    else:
        print('✨ ReForge is already unpacked. Skipping download.')
else:
    print("❌ FATAL: Could not determine root directory. Halting ReForge installation.")
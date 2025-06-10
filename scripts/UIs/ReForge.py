# /content/ANXETY/scripts/UIs/ReForge.py (Corrected and Robust Version)

import os
import sys
from pathlib import Path
import subprocess

# --- Self-aware pathing to find the project root ---
try:
    ANXETY_ROOT = Path(__file__).resolve().parents[2]
except NameError:
    ANXETY_ROOT = Path.cwd()

# Add the modules directory to the Python path
sys.path.insert(0, str(ANXETY_ROOT / 'modules'))
# --- End of fix ---

import json_utils as js

def get_webui_install_path():
    """Reads the definitive webui_path from settings.json."""
    settings_path = ANXETY_ROOT / 'settings.json'
    if not settings_path.exists():
        print("❌ FATAL: settings.json not found. Cannot determine installation path.")
        return None
    
    webui_settings = js.read(settings_path, 'WEBUI', {})
    install_path = webui_settings.get('webui_path')
    
    if not install_path:
        print("❌ FATAL: 'webui_path' not defined in settings.json.")
        return None
        
    return Path(install_path)

def main():
    install_dir = get_webui_install_path()
    if not install_dir:
        sys.exit(1) # Exit with an error code if the path is invalid

    git_repo_url = 'https://github.com/huchenlei/stable-diffusion-webui-reforge.git'

    if not install_dir.exists():
        print(f'✅ Cloning ReForge repository into: {install_dir}')
        # Using check=True will raise an error if git clone fails
        try:
            subprocess.run(
                ['git', 'clone', '-b', 'master', '--depth', '1', git_repo_url, str(install_dir)],
                check=True,
                capture_output=True, # Capture output to prevent flooding the notebook
                text=True
            )
            print('✅ Unpacking ReForge Complete!')
        except subprocess.CalledProcessError as e:
            print("❌❌❌ GIT CLONE FAILED! ❌❌❌")
            print(f"The attempt to clone the ReForge WebUI failed. This is a critical error.")
            print(f"Error details (stderr):\n{e.stderr}")
            sys.exit(1) # Halt execution
    else:
        print(f'✨ ReForge directory already exists at {install_dir}. Skipping download.')

if __name__ == '__main__':
    main()
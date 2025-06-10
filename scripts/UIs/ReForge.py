# /content/ANXETY/scripts/UIs/ReForge.py (Final Version with Error Reporting)

import os
import sys
from pathlib import Path
import subprocess

# --- Self-aware pathing ---
try:
    ANXETY_ROOT = Path(__file__).resolve().parents[2]
except NameError:
    ANXETY_ROOT = Path.cwd()
sys.path.insert(0, str(ANXETY_ROOT / 'modules'))
# ---

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
        sys.exit(1)

    git_repo_url = 'https://github.com/huchenlei/stable-diffusion-webui-reforge.git'

    if not install_dir.exists():
        print(f'✅ Cloning ReForge repository into: {install_dir}')
        try:
            # --- MODIFIED FOR DEBUGGING ---
            # This version captures output to manually print it on error.
            result = subprocess.run(
                ['git', 'clone', '-b', 'master', '--depth', '1', git_repo_url, str(install_dir)],
                check=True,
                capture_output=True,
                text=True
            )
            # --- END MODIFICATION ---
            print('✅ Unpacking ReForge Complete!')
        except subprocess.CalledProcessError as e:
            print("❌❌❌ GIT CLONE FAILED! ❌❌❌")
            print(f"The attempt to clone the ReForge WebUI failed with exit code {e.returncode}.")
            print("\n--- Captured Standard Output (stdout) ---")
            print(e.stdout if e.stdout else "[No standard output]")
            print("\n--- Captured Standard Error (stderr) ---")
            print(e.stderr if e.stderr else "[No standard error]")
            print("-" * 40)
            sys.exit(1) # Halt execution
    else:
        print(f'✨ ReForge directory already exists at {install_dir}. Skipping download.')

if __name__ == '__main__':
    main()
# @title 1.0 - Bootstrap, Patch, and Launch (File-Based)
# @markdown This cell downloads the project files, repairs the VENV, and starts the UI.

print(" S T A R T I N G  A N X I E T Y L I G H T N I N G  S E T U P ")
print("="*60)

import os
import sys
from pathlib import Path
import subprocess

# --- Define Paths ---
ANXETY_ROOT = Path('/content/ANXETY')
scripts_dir = ANXETY_ROOT / 'scripts'
setup_script_path = scripts_dir / 'setup.py'

# --- Define the new setup.py content ---
# This script will download all other project files from GitHub.
setup_py_content = r'''
import subprocess
import shlex
import sys
from pathlib import Path

REPO_URL = "drf0rk/AnxietyLightning"
BRANCH = "main"
DEST_DIR = Path("/content/ANXETY")

def run_command(command, description):
    print(f"🔩 Executing: {description}...")
    try:
        process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in iter(process.stdout.readline, ''):
            print(f"  > {line.strip()}")
        process.wait()
        if process.returncode == 0:
            print(f"✅ Success: {description} completed.")
            return True
        else:
            print(f"❌ Error: {description} failed with code {process.returncode}.")
            return False
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}"); return False

def main():
    print("--- Starting Project File Download ---")
    DEST_DIR.mkdir(parents=True, exist_ok=True)
    if subprocess.run(['degit', '--version'], capture_output=True).returncode != 0:
        print("🔧 'degit' not found. Attempting to install via npm...")
        if not run_command("npm install -g degit", "Install degit"):
            sys.exit(1)
    print(f"\nDownloading repository '{REPO_URL}'...")
    if not run_command(f"degit {REPO_URL}#{BRANCH} {DEST_DIR} --force", "Download repository files"):
        sys.exit(1)
    print("\n✅ All project files have been downloaded successfully.")

if __name__ == "__main__":
    main()
'''

# --- Main Execution Block ---
try:
    # 1. Write the setup script to disk
    print("⚙️  Preparing the project downloader...")
    scripts_dir.mkdir(parents=True, exist_ok=True)
    setup_script_path.write_text(setup_py_content)
    print(f"✅ Setup script written to: {setup_script_path}")

    # 2. Run the setup script to download all project files
    print("\n" + "="*60)
    get_ipython().run_line_magic('run', str(setup_script_path))

    # 3. Perform VENV download and repair (if necessary)
    print("\n" + "="*60)
    print("--- Checking VENV Status ---")
    venv_downloader_script = scripts_dir / 'en' / 'downloading-en.py'
    if Path('/content/venv').exists():
        print("✅ VENV already exists. Skipping download.")
    elif venv_downloader_script.exists():
        get_ipython().run_line_magic('run', str(venv_downloader_script))
    else:
        print("❌ VENV downloader script not found. Cannot proceed.")
        raise FileNotFoundError(str(venv_downloader_script))
    
    # VENV Repair Logic
    print("\n--- Applying VENV Patches & Fixes ---")
    VENV_BIN_PATH = Path('/content/venv/bin')
    VENV_PYTHON_EXEC = VENV_BIN_PATH / 'python'
    if VENV_BIN_PATH.exists():
        print("  - Upgrading core libraries for compatibility...")
        try:
            subprocess.run([str(VENV_PYTHON_EXEC), '-m', 'pip', 'install', '--upgrade', 'torch', 'torchvision', 'xformers', '--index-url', 'https://download.pytorch.org/whl/cu121'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
            print("  ✅ Core libraries upgraded successfully.")
        except subprocess.CalledProcessError:
            print(f"  ❌ Library upgrade failed.")
    else:
        print("⚠️ VENV not found. Skipping patches.")

    # 4. Start the main user interface
    print("\n" + "="*60)
    print("✅✅✅ Setup complete! Starting main interface... ✅✅✅")
    main_ui_script = scripts_dir / 'en' / 'widgets-en.py'
    if main_ui_script.exists():
        get_ipython().run_line_magic('run', str(main_ui_script))
    else:
        print(f"❌ Main UI script not found at {main_ui_script}")

except Exception as e:
    print(f"\n❌ An unrecoverable error occurred during the bootstrap process: {e}")
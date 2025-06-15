# /scripts/_bootstrap.py

import os
import sys
from pathlib import Path
import subprocess
import runpy
import shlex

def run_command(command, description):
    """Runs a shell command, ensuring it's visible in the logs."""
    print(f"🔩 Executing: {description}...")
    try:
        process = subprocess.Popen(
            shlex.split(command),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding='utf-8',
            errors='replace'
        )
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
        print(f"❌ An unexpected error occurred: {e}")
        return False

def main():
    """The main bootstrap and execution function."""
    print("--- 🚀 AnxietyLightning Bootstrapper Initializing ---")

    # --- 1. Define Core Paths & Environment ---
    HOME_DIR = Path('/content')
    ANXETY_ROOT = HOME_DIR / 'ANXETY'
    SCRIPTS_DIR = ANXETY_ROOT / 'scripts'
    LOG_DIR = ANXETY_ROOT / "logs"

    os.environ['HOME_DIR'] = str(HOME_DIR)
    os.environ['ANXETY_ROOT'] = str(ANXETY_ROOT)
    
    # --- 2. Synchronize Project Files ---
    print("\\n--- 🚀 Stage 1: Synchronizing Project Repository ---")
    ANXETY_ROOT.mkdir(parents=True, exist_ok=True)
    
    # Use degit for fast repo cloning
    if not run_command("npm install -g degit", "Install degit"):
        sys.exit(1)
    
    degit_command = f"degit drf0rk/AnxietyLightning#main {ANXETY_ROOT} --force"
    if not run_command(degit_command, "Download repository files"):
        sys.exit(1)

    LOG_DIR.mkdir(exist_ok=True)
    print(f"✅ Log directory ensured at {LOG_DIR}")

    # Add project to Python's path
    if str(ANXETY_ROOT) not in sys.path:
        sys.path.insert(0, str(ANXETY_ROOT))

    # --- 3. Install Dependencies ---
    print("\\n--- 🚀 Stage 2: Installing Dependencies ---")
    try:
        import gradio
    except ImportError:
        print("Installing Gradio...")
        subprocess.run([sys.executable, "-m", "pip", "install", "gradio"], check=True)

    # --- 4. Launch the UI ---
    print("\\n--- 🚀 Stage 3: Launching Gradio UI ---")
    ui_script_path = SCRIPTS_DIR / '_ui.py'
    if not ui_script_path.exists():
        print(f"❌ FATAL: UI script not found at {ui_script_path} after sync.")
        sys.exit(1)
        
    # Use runpy to execute the UI script
    try:
        print(f"Executing UI from: {ui_script_path}")
        runpy.run_path(str(ui_script_path))
    except Exception as e:
        print(f"❌ FATAL: Failed to launch the UI. Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

    print("\\n--- ✅ Bootstrap process complete. UI should be running. ---")


if __name__ == "__main__":
    # This allows the script to be executed directly.
    # The notebook will call this with `%run _bootstrap.py`
    main()
# /content/ANXETY/scripts/launch.py (Definitive Final Version)

import os
import sys
from pathlib import Path
import subprocess

# --- Self-aware pathing ---
try:
    ANXETY_ROOT = Path(__file__).resolve().parents[1]
except NameError:
    # Fallback for environments where __file__ is not defined
    ANXETY_ROOT = Path.cwd() / 'ANXETY'
if str(ANXETY_ROOT) not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT / 'modules'))
# ---

import json_utils as js

# --- Configuration ---
SETTINGS_PATH = ANXETY_ROOT / 'settings.json'

def get_launch_config():
    """Reads all necessary configuration for launch from settings.json."""
    webui_settings = js.read(SETTINGS_PATH, 'WEBUI', {})
    widget_settings = js.read(SETTINGS_PATH, 'WIDGETS', {})

    if not webui_settings or not widget_settings:
        print("❌ FATAL: WEBUI or WIDGETS configuration is missing from settings.json.")
        return None

    config = {
        "name": webui_settings.get("current"),
        "path": Path(webui_settings.get("webui_path")),
        "args": widget_settings.get("commandline_arguments", "")
    }

    if not all(config.values()):
        print(f"❌ FATAL: Incomplete launch configuration: {config}")
        return None

    return config

def main():
    """Main launch function."""
    config = get_launch_config()
    if not config:
        sys.exit(1)

    webui_name = config["name"]
    webui_path = config["path"]
    args = config["args"]

    if not webui_path.exists():
        print(f"❌ FATAL: The WebUI directory does not exist at the configured path: {webui_path}")
        print("Please re-run the 'Downloading' cell to install the WebUI.")
        sys.exit(1)

    # Determine the correct launch script name based on the UI
    if webui_name == "ComfyUI":
        launch_script_name = "main.py"
    else:
        launch_script_name = "launch.py" # For A1111, Forge, ReForge, SD-UX

    launch_script_path = webui_path / launch_script_name
    if not launch_script_path.exists():
        print(f"❌ FATAL: Could not find the launch script '{launch_script_name}' in {webui_path}")
        sys.exit(1)

    # Change into the WebUI's directory before launching
    os.chdir(webui_path)

    print(f"✅ Changed directory to: {os.getcwd()}")
    print(f"🚀 Launching {webui_name} with arguments: {args}")
    print("-" * 60)

    # Construct the final command
    command = [sys.executable, launch_script_name] + args.split()
    
    # Use subprocess.run without capturing output so we can see the WebUI logs
    subprocess.run(command)

if __name__ == '__main__':
    # Add a try-except block to gracefully handle KeyboardInterrupt
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n✅ Launch interrupted by user. Process terminated.")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred during launch: {e}")
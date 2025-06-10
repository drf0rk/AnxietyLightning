# /content/ANXETY/scripts/launch.py (Final Robust Version)

import os
import sys
from pathlib import Path
import subprocess
import argparse

# --- Self-aware pathing ---
try:
    ANXETY_ROOT = Path(__file__).resolve().parents[1]
except NameError:
    ANXETY_ROOT = Path.cwd()
if str(ANXETY_ROOT / 'modules') not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT / 'modules'))
# ---

import json_utils as js

# --- Configuration ---
SETTINGS_PATH = ANXETY_ROOT / 'settings.json'

def get_launch_config():
    """Reads all necessary configuration for launch from settings.json."""
    webui_settings = js.read(SETTINGS_PATH, 'WEBUI', {})
    widget_settings = js.read(SETTINGS_PATH, 'WIDGETS', {})
    env_settings = js.read(SETTINGS_PATH, 'ENVIRONMENT', {})

    if not all([webui_settings, widget_settings, env_settings]):
        print("❌ FATAL: One or more configuration sections (WEBUI, WIDGETS, ENVIRONMENT) are missing from settings.json.")
        return None

    config = {
        "name": webui_settings.get("current"), "path": Path(webui_settings.get("webui_path")),
        "args": widget_settings.get("commandline_arguments", ""), "env_name": env_settings.get("env_name")
    }

    if not all(config.values()):
        print(f"❌ FATAL: Incomplete launch configuration: {config}")
        return None

    return config

def main(args):
    """Main launch function."""
    config = get_launch_config()
    if not config: sys.exit(1)

    webui_name, webui_path, cli_args_str, env_name = config["name"], config["path"], config["args"], config["env_name"]

    if not webui_path.exists():
        print(f"❌ FATAL: WebUI directory does not exist: {webui_path}. Please re-run the 'Downloading' cell."); sys.exit(1)

    launch_script_name = "main.py" if webui_name == "ComfyUI" else "launch.py"
    launch_script_path = webui_path / launch_script_name
    
    if not launch_script_path.exists():
        print(f"❌ FATAL: Launch script not found: '{launch_script_path}'"); sys.exit(1)

    os.chdir(webui_path)
    print(f"✅ Changed directory to: {os.getcwd()}")
    
    final_args = cli_args_str.split()
    if '--share' in final_args: final_args.remove('--share')
    if env_name in ["Google Colab", "Kaggle", "Lightning AI"] and '--listen' not in final_args:
        final_args.append('--listen')
        
    print(f"🚀 Launching {webui_name} with arguments: {' '.join(final_args)}")
    print("-" * 60)

    command = [sys.executable, str(launch_script_path)] + final_args
    
    # --- FIX: Use Popen and manually pipe stdout/stderr to ensure all output is displayed ---
    # This prevents the cell from finishing silently if the subprocess exits immediately.
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1, universal_newlines=True)

    for line in iter(process.stdout.readline, ''):
        sys.stdout.write(line)
        sys.stdout.flush()
    
    process.stdout.close()
    return_code = process.wait()

    if return_code:
        print(f"\n❌ WebUI process exited with error code {return_code}.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="AnxietyLightning Launcher")
    parser.add_argument('-l', '--log-tunnels', action='store_true', help='Enable detailed logging for tunnels.')
    parsed_args, _ = parser.parse_known_args()
    
    try:
        main(parsed_args)
    except KeyboardInterrupt:
        print("\n\n✅ Launch interrupted by user. Process terminated.")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred during launch: {e}")
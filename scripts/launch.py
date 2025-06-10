# /content/ANXETY/scripts/launch.py (Final Version with Correct --data-dir Argument)

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
# --- FIX: Define the shared model base path here ---
HOME = Path(js.read(SETTINGS_PATH, 'ENVIRONMENT.home_path', str(Path.home())))
SHARED_MODEL_BASE = HOME / 'sd_models_shared'
# --- END FIX ---

def get_launch_config():
    """Reads all necessary configuration for launch from settings.json."""
    webui_settings = js.read(SETTINGS_PATH, 'WEBUI', {})
    widget_settings = js.read(SETTINGS_PATH, 'WIDGETS', {})
    env_settings = js.read(SETTINGS_PATH, 'ENVIRONMENT', {})

    if not all([webui_settings, widget_settings, env_settings]):
        print("❌ FATAL: One or more configuration sections are missing.")
        return None

    return {
        "webui_settings": webui_settings,
        "widget_settings": widget_settings,
        "env_settings": env_settings
    }

def main(args):
    """Main launch function."""
    config = get_launch_config()
    if not config: sys.exit(1)

    webui_name = config["webui_settings"].get("current")
    webui_path = Path(config["webui_settings"].get("webui_path"))
    cli_args_str = config["widget_settings"].get("commandline_arguments", "")
    env_name = config["env_settings"].get("env_name")

    if not webui_path.exists():
        print(f"❌ FATAL: WebUI directory does not exist: {webui_path}."); sys.exit(1)

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

    # --- FIX: Use --data-dir to point to the top-level shared folder ---
    # This is the correct way to tell ReForge where to find all its data subdirectories.
    final_args.extend(['--data-dir', str(SHARED_MODEL_BASE)])
    # --- END FIX ---
        
    print(f"🚀 Launching {webui_name} with arguments: {' '.join(final_args)}")
    print("-" * 60)

    command = [sys.executable, str(launch_script_path)] + final_args
    
    subprocess.run(command)

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
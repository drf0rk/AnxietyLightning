# scripts/en/downloading-en.py

import os
import sys
import subprocess
from pathlib import Path

# Self-aware pathing
try:
    # --- CORRECTED LINE ---
    # From .../scripts/en/ the root is 2 levels up
    ANXETY_ROOT = Path(__file__).resolve().parents[2]
    # --- END CORRECTION ---
except NameError:
    # Fallback for environments where __file__ is not defined
    ANXETY_ROOT = Path.cwd()

sys.path.append(str(ANXETY_ROOT))

from modules.json_utils import JsonUtils
from modules.Manager import Manager

WEBUI_DIR_MAPPING = {
    'A1111': 'stable-diffusion-webui',
    'Forge': 'stable-diffusion-webui-forge',
    'ReForge': 'stable-diffusion-webui-reforge',
    'Classic': 'stable-diffusion-webui-classic',
    'ComfyUI': 'ComfyUI',
    'SD-UX': 'stable-diffusion-webui-ux'
}

SETTINGS_PATH = ANXETY_ROOT / 'settings.json'
SCRIPTS_UIs = ANXETY_ROOT / 'scripts' / 'UIs'
DOWNLOAD_RESULT_PY = ANXETY_ROOT / 'scripts' / 'download-result.py'

js = JsonUtils()

def get_webui_path():
    """Reads settings and returns the constructed path to the WebUI."""
    try:
        widgets_settings = js.read(SETTINGS_PATH, 'WIDGETS')
        env_settings = js.read(SETTINGS_PATH, 'ENVIRONMENT')

        if not widgets_settings or not env_settings:
            print("❌ Error reading WIDGETS or ENVIRONMENT from settings.json")
            return None, None

        webui_name = widgets_settings.get('WebUI')
        root_dir = Path(env_settings.get('root_dir', ''))
        
        if not webui_name or not root_dir.is_dir():
            print(f"❌ Invalid WebUI name ('{webui_name}') or root directory ('{root_dir}').")
            return None, None
        
        webui_dir_name = WEBUI_DIR_MAPPING.get(webui_name, webui_name)
        
        return root_dir / webui_dir_name, webui_name

    except Exception as e:
        print(f"❌ An error occurred in get_webui_path: {e}")
        return None, None

def main():
    """Main execution function."""
    print(f"✅ Attempting to run script from: {__file__}")

    WEBUI_PATH, webui_name = get_webui_path()
    if not WEBUI_PATH:
        return

    if not WEBUI_PATH.exists():
        print(f"⌚ Unpacking Stable Diffusion | WEBUI: {webui_name}...")
        script_path = SCRIPTS_UIs / f'{webui_name}.py'
        if script_path.exists():
            subprocess.run([sys.executable, str(script_path)], check=True)
        else:
            print(f"❌ Installer script not found for {webui_name} at {script_path}")
            return
    else:
        print(f"🔧 Current WebUI: {webui_name} | Already installed.")

    settings = js.read(SETTINGS_PATH, 'WIDGETS')
    latest_webui = settings.get('update_webui', False)
    latest_extensions = settings.get('update_extensions', False)
    
    if latest_webui or latest_extensions:
        print("⌚️ Updating WebUI and Extensions...")
        if latest_webui and (WEBUI_PATH / '.git').exists():
            subprocess.run(['git', '-C', str(WEBUI_PATH), 'pull'], check=True)
        
        extension_dir = WEBUI_PATH / 'extensions'
        if latest_extensions and extension_dir.exists():
            for entry in os.listdir(str(extension_dir)):
                dir_path = os.path.join(str(extension_dir), entry)
                if os.path.isdir(dir_path) and os.path.exists(os.path.join(dir_path, '.git')):
                    print(f"  - Updating extension: {entry}")
                    subprocess.run(['git', '-C', dir_path, 'pull'], check=True)
        print("✨ Update WebUI and Extensions Complete!")

    print("📦 Processing asset download selections...")
    if settings.get('download_manager', False):
        manager = Manager(SETTINGS_PATH)
        manager.run()
    else:
        print("Download Manager disabled. Skipping asset downloads.")

    print("🏁 Download processing complete!")
    subprocess.run([sys.executable, str(DOWNLOAD_RESULT_PY)])

if __name__ == "__main__":
    main()
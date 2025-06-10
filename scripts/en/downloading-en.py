# /content/ANXETY/scripts/en/downloading-en.py (Corrected and Finalized)

import os
import sys
from pathlib import Path
import subprocess

# --- Self-aware pathing to find the project root ---
try:
    ANXETY_ROOT = Path(__file__).resolve().parents[2]
except NameError:
    ANXETY_ROOT = Path.cwd()

sys.path.insert(0, str(ANXETY_ROOT))
sys.path.insert(0, str(ANXETY_ROOT / 'modules'))

# --- Corrected Imports ---
import modules.json_utils as js
from modules.Manager import m_download

# --- Constants ---
SETTINGS_PATH = ANXETY_ROOT / 'settings.json'
SCRIPTS_UIs = ANXETY_ROOT / 'scripts' / 'UIs'
DOWNLOAD_RESULT_PY = ANXETY_ROOT / 'scripts' / 'download-result.py'
WEBUI_DIR_MAPPING = {
    'A1111': 'A1111', 'Forge': 'Forge', 'ReForge': 'ReForge',
    'Classic': 'Classic', 'ComfyUI': 'ComfyUI', 'SD-UX': 'SD-UX'
}

def get_webui_path():
    """Reads the current WebUI path from settings."""
    try:
        webui_settings = js.read(SETTINGS_PATH, 'WEBUI', {})
        webui_path = webui_settings.get('webui_path')
        webui_name = webui_settings.get('current')
        return Path(webui_path) if webui_path else None, webui_name
    except Exception as e:
        print(f"❌ Error in get_webui_path: {e}")
        return None, None

def read_data_file(file_path, data_key):
    """Reads a specific dictionary from a Python data file."""
    local_vars = {}
    if not file_path.exists(): return {}
    with open(file_path, 'r', encoding='utf-8') as f:
        exec(f.read(), {}, local_vars)
    return local_vars.get(data_key, {})

def process_selections(selections, data_dict, prefix, dst_dir):
    """Processes widget selections and returns a list of download commands."""
    commands = []
    if not isinstance(selections, (list, tuple)): return commands

    all_models = list(data_dict.keys())
    for selection in selections:
        if selection == 'none' or not selection: continue
        if selection == 'ALL':
            for model_name, model_info_list in data_dict.items():
                for model_info in model_info_list:
                    commands.append(f"{prefix}:{model_info['url']}[{model_info.get('name', '')}]")
            continue

        model_name = selection.split('. ', 1)[-1]
        if model_name in data_dict:
            for model_info in data_dict[model_name]:
                commands.append(f"{prefix}:{model_info['url']}[{model_info.get('name', '')}]")
    return commands

def main():
    """Main execution function for the downloading script."""
    print(f"✅ Running download orchestrator: {__file__}")

    settings = js.read(SETTINGS_PATH, 'WIDGETS', {})
    webui_paths = js.read(SETTINGS_PATH, 'WEBUI', {})

    if not settings or not webui_paths:
        print("❌ Critical settings missing. Cannot proceed with downloads.")
        return

    WEBUI_PATH, webui_name = get_webui_path()
    if not WEBUI_PATH or not webui_name:
        print("❌ Halting due to missing WebUI configuration.")
        return

    # 1. Install or Verify WebUI
    if not WEBUI_PATH.exists():
        print(f"🚀 Unpacking Stable Diffusion | WEBUI: {webui_name}...")
        installer_script = SCRIPTS_UIs / f"{WEBUI_DIR_MAPPING.get(webui_name, webui_name)}.py"
        if installer_script.exists():
            subprocess.run([sys.executable, str(installer_script)], check=True)
        else:
            print(f"❌ Installer script not found: {installer_script}")
            return
    else:
        print(f"🔧 WebUI found: {webui_name}")

    # 2. Process Asset Downloads
    print("📦 Processing asset download selections from settings...")
    is_xl = settings.get('XL_models', False)
    all_commands = []

    models_py = ANXETY_ROOT / 'scripts' / ('_xl-models-data.py' if is_xl else '_models-data.py')
    loras_py = ANXETY_ROOT / 'scripts' / '_loras-data.py'

    model_data = read_data_file(models_py, 'sdxl_models_data' if is_xl else 'sd15_model_data')
    vae_data = read_data_file(models_py, 'sdxl_vae_data' if is_xl else 'sd15_vae_data')
    lora_data = read_data_file(loras_py, 'lora_data').get('sdxl_loras' if is_xl else 'sd15_loras', {})
    cnet_data = read_data_file(models_py, 'controlnet_list')

    all_commands.extend(process_selections(settings.get('model', []), model_data, 'model', webui_paths.get('model_dir')))
    all_commands.extend(process_selections(settings.get('vae', []), vae_data, 'vae', webui_paths.get('vae_dir')))
    all_commands.extend(process_selections(settings.get('lora', []), lora_data, 'lora', webui_paths.get('lora_dir')))
    all_commands.extend(process_selections(settings.get('controlnet', []), cnet_data, 'control', webui_paths.get('control_dir')))

    if all_commands:
        download_line = ", ".join(all_commands)
        print(f"▶️  Executing downloads...")
        m_download(download_line, log=True, unzip=True)
    else:
        print("⏩ No assets selected from dropdowns.")

    print("🏁 Download processing complete!")
    if DOWNLOAD_RESULT_PY.exists():
        subprocess.run([sys.executable, str(DOWNLOAD_RESULT_PY)])

if __name__ == "__main__":
    main()
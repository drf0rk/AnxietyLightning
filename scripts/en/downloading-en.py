# /content/ANXETY/scripts/en/downloading-en.py (Final Orchestrator Version)

import os
import sys
from pathlib import Path
import subprocess
import re

# --- Self-aware pathing to fix ModuleNotFoundError ---
try:
    ANXETY_ROOT = Path(__file__).resolve().parents[2]
except NameError:
    ANXETY_ROOT = Path.cwd()

if str(ANXETY_ROOT) not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT))
if str(ANXETY_ROOT / 'modules') not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT / 'modules'))
# --- End of fix ---

import modules.json_utils as js
from modules.Manager import m_download, m_clone

# --- Constants ---
SETTINGS_PATH = ANXETY_ROOT / 'settings.json'
SCRIPTS_UIs = ANXETY_ROOT / 'scripts' / 'UIs'
WEBUI_DIR_MAPPING = {
    'A1111': 'A1111', 'Forge': 'Forge', 'ReForge': 'ReForge',
    'Classic': 'Classic', 'ComfyUI': 'ComfyUI', 'SD-UX': 'SD-UX'
}

def get_webui_path():
    try:
        webui_settings = js.read(SETTINGS_PATH, 'WEBUI', {})
        webui_path = webui_settings.get('webui_path')
        webui_name = webui_settings.get('current')
        return Path(webui_path) if webui_path else None, webui_name
    except Exception as e:
        print(f"❌ Error in get_webui_path: {e}")
        return None, None

def read_data_file(file_path, data_key):
    local_vars = {}
    if not file_path.exists(): return {}
    with open(file_path, 'r', encoding='utf-8') as f: exec(f.read(), {}, local_vars)
    return local_vars.get(data_key, {})

def process_selections(selections, data_dict, prefix):
    """Generates a list of prefixed download commands: 'prefix:url[name]'."""
    commands = []
    if not isinstance(selections, (list, tuple)): return commands
    for selection in selections:
        if selection == 'none' or not selection: continue
        if selection == 'ALL':
            for model_name, model_data_value in data_dict.items():
                model_info_list = model_data_value if isinstance(model_data_value, list) else [model_data_value]
                for model_info in model_info_list:
                    if isinstance(model_info, dict):
                        commands.append(f"{prefix}:{model_info['url']}[{model_info.get('name', '')}]")
            continue
        model_name = selection.split('. ', 1)[-1]
        if model_name in data_dict:
            model_data_value = data_dict[model_name]
            model_info_list = model_data_value if isinstance(model_data_value, list) else [model_data_value]
            for model_info in model_info_list:
                if isinstance(model_info, dict):
                    commands.append(f"{prefix}:{model_info['url']}[{model_info.get('name', '')}]")
    return commands

def main():
    print(f"✅ Running download orchestrator: {__file__}")
    settings = js.read(SETTINGS_PATH, 'WIDGETS', {})
    webui_paths = js.read(SETTINGS_PATH, 'WEBUI', {})
    if not settings or not webui_paths:
        print("❌ Critical settings missing. Cannot proceed.")
        return

    WEBUI_PATH, webui_name = get_webui_path()
    if not WEBUI_PATH or not webui_name:
        print("❌ Halting due to missing WebUI configuration.")
        return

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

    print("📦 Processing asset download selections from settings...")
    is_xl = settings.get('XL_models', False)
    all_commands = []
    
    models_py_path = ANXETY_ROOT / 'scripts' / ('_xl-models-data.py' if is_xl else '_models-data.py')
    loras_py_path = ANXETY_ROOT / 'scripts' / '_loras-data.py'
    
    model_data = read_data_file(models_py_path, 'sdxl_models_data' if is_xl else 'sd15_model_data')
    vae_data = read_data_file(models_py_path, 'sdxl_vae_data' if is_xl else 'sd15_vae_data')
    lora_data = read_data_file(loras_py_path, 'lora_data').get('sdxl_loras' if is_xl else 'sd15_loras', {})
    cnet_data = read_data_file(models_py_path, 'controlnet_list')

    all_commands.extend(process_selections(settings.get('model', []), model_data, 'model'))
    all_commands.extend(process_selections(settings.get('vae', []), vae_data, 'vae'))
    all_commands.extend(process_selections(settings.get('lora', []), lora_data, 'lora'))
    all_commands.extend(process_selections(settings.get('controlnet', []), cnet_data, 'control'))

    # --- THIS IS THE NEW ORCHESTRATION LOGIC ---
    if not all_commands:
        print("⏩ No assets were selected for download.")
    else:
        print(f"▶️  Orchestrating downloads for {len(all_commands)} assets...")
        
        # Mapping prefixes to their destination directories from settings.json
        PREFIX_PATH_MAP = {
            'model': webui_paths.get('model_dir'),
            'vae': webui_paths.get('vae_dir'),
            'lora': webui_paths.get('lora_dir'),
            'control': webui_paths.get('control_dir'),
            'extension': webui_paths.get('extension_dir')
            # Add other prefixes here if needed (embed, upscale, etc.)
        }

        for command in all_commands:
            try:
                prefix, rest = command.split(':', 1)
                if prefix not in PREFIX_PATH_MAP:
                    print(f"  - ⚠️ Skipping unknown prefix '{prefix}' in command: {command}")
                    continue

                url_match = re.match(r"(.*?)(?:\[(.*?)\])?$", rest)
                url = url_match.group(1)
                filename = url_match.group(2) if url_match.group(2) else ""

                dst_dir = PREFIX_PATH_MAP[prefix]

                if not dst_dir:
                    print(f"  - ⚠️ Skipping command, no destination directory defined for prefix '{prefix}'")
                    continue
                
                # For extensions, we use m_clone
                if prefix == 'extension':
                    print(f"  - 🌀 Cloning extension from {url} into {dst_dir}")
                    m_clone(f"git clone --depth 1 {url} {os.path.join(dst_dir, filename)}")
                else:
                    # For files, we use m_download with the simple format
                    print(f"  - 🔽 Downloading '{filename or url.split('/')[-1]}' to {dst_dir}")
                    m_download(f'"{url}" "{dst_dir}" "{filename}"', log=True, unzip=True)

            except Exception as e:
                print(f"  - ❌ Failed to process command '{command}': {e}")
                
    print("🏁 Download processing complete!")
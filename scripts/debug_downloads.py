# /content/ANXETY/scripts/debug_downloads.py

import os
import sys
from pathlib import Path

# --- Setup Paths ---
try:
    ANXETY_ROOT = Path(__file__).resolve().parents[1]
except NameError:
    ANXETY_ROOT = Path.cwd()

if str(ANXETY_ROOT) not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT))
if str(ANXETY_ROOT / 'modules') not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT / 'modules'))

import modules.json_utils as js

print("--- 🕵️ ANXETY DOWNLOAD DEBUGGER 🕵️ ---\n")

# --- 1. Load Settings ---
SETTINGS_PATH = ANXETY_ROOT / 'settings.json'
if not SETTINGS_PATH.exists():
    print("❌ FATAL: settings.json does not exist. Cannot run debug.")
    sys.exit(1)

widget_settings = js.read(SETTINGS_PATH, 'WIDGETS', {})
webui_paths = js.read(SETTINGS_PATH, 'WEBUI', {})

if not widget_settings or not webui_paths:
    print("❌ FATAL: WIDGETS or WEBUI section is missing from settings.json.")
    sys.exit(1)

print("✅ Settings files loaded successfully.\n")

# --- 2. Display Critical Paths ---
print("--- 🗺️ Critical Paths Verification 🗺️ ---")
print(f"  - ANXETY Root: {ANXETY_ROOT}")
print(f"  - Models Directory: {webui_paths.get('model_dir')}")
print(f"  - VAE Directory: {webui_paths.get('vae_dir')}")
print(f"  - LoRA Directory: {webui_paths.get('lora_dir')}")
print(f"  - ControlNet Directory: {webui_paths.get('control_dir')}")
print("-" * 40)

# --- 3. Re-create Download Commands ---
print("\n--- 📝 Reconstructing Download Commands 📝 ---")
is_xl = widget_settings.get('XL_models', False)
print(f"  - Mode: {'SDXL' if is_xl else 'SD 1.5'}")

# Dummy function to simulate processing
def process_selections_debug(selections, data_dict, prefix):
    commands = []
    if not isinstance(selections, (list, tuple)): return commands
    for selection in selections:
        if selection == 'none' or not selection: continue
        if selection == 'ALL':
            # Simplified for debug
            commands.append(f"{prefix}:ALL_MODELS_SELECTED")
            continue
        model_name = selection.split('. ', 1)[-1]
        if model_name in data_dict:
            model_data_value = data_dict[model_name]
            model_info_list = model_data_value if isinstance(model_data_value, list) else [model_data_value]
            for model_info in model_info_list:
                if isinstance(model_info, dict):
                    commands.append(f"{prefix}:{model_info['url']}[{model_info.get('name', 'NO_NAME_SPECIFIED')}]")
    return commands

models_py_path = ANXETY_ROOT / 'scripts' / ('_xl-models-data.py' if is_xl else '_models-data.py')
loras_py_path = ANXETY_ROOT / 'scripts' / '_loras-data.py'

model_data = js.read_data_file(models_py_path, 'sdxl_models_data' if is_xl else 'sd15_model_data')
vae_data = js.read_data_file(models_py_path, 'sdxl_vae_data' if is_xl else 'sd15_vae_data')
lora_data = js.read_data_file(loras_py_path, 'lora_data').get('sdxl_loras' if is_xl else 'sd15_loras', {})
cnet_data = js.read_data_file(models_py_path, 'controlnet_list')

all_commands = []
all_commands.extend(process_selections_debug(widget_settings.get('model', []), model_data, 'model'))
all_commands.extend(process_selections_debug(widget_settings.get('vae', []), vae_data, 'vae'))
all_commands.extend(process_selections_debug(widget_settings.get('lora', []), lora_data, 'lora'))
all_commands.extend(process_selections_debug(widget_settings.get('controlnet', []), cnet_data, 'control'))

if not all_commands:
    print("  - ‼️ No download commands were generated from your selections.")
else:
    print("  - ✅ The following commands would be sent to the download manager:")
    for i, cmd in enumerate(all_commands):
        print(f"    {i+1}: {cmd}")

print("-" * 40)
print("\n--- ✅ Debugging Complete ---")
print("If paths look incorrect or commands are missing, the issue is with settings.json or the data files.")
print("If everything looks correct here, the issue is likely within modules/Manager.py or the underlying download tools.")
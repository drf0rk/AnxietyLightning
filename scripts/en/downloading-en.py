# ~ download.py | by ANXETY ~ (Final Path Correction)

import os
import re
import sys
import json
import time
import shlex
import shutil
import subprocess
from pathlib import Path
from datetime import timedelta
from urllib.parse import urlparse
from IPython import get_ipython
from IPython.display import clear_output
from IPython.utils import capture

# --- Get the correct paths from settings.json ---
anxety_path = Path.home() / 'ANXETY'
modules_path = anxety_path / 'modules'
if str(modules_path) not in sys.path:
    sys.path.insert(0, str(modules_path))

import json_utils as js
from webui_utils import handle_setup_timer
from CivitaiAPI import CivitAiAPI
from Manager import m_download

# Load all settings and paths from the settings file
settings_path = anxety_path / 'settings.json'
settings = js.read(settings_path)
env_settings = settings.get('ENVIRONMENT', {})
widget_settings = settings.get('WIDGETS', {})
webui_settings = settings.get('WEBUI', {})

# Define all necessary paths from the loaded settings
SCRIPTS = Path(env_settings.get('scr_path')) / 'scripts'
UI = webui_settings.get('current')
WEBUI_PATH = Path(webui_settings.get('webui_path'))
extension_dir = Path(webui_settings.get('extension_dir'))
model_dir = Path(webui_settings.get('model_dir'))
vae_dir = Path(webui_settings.get('vae_dir'))
lora_dir = Path(webui_settings.get('lora_dir'))
control_dir = Path(webui_settings.get('control_dir'))

# Get widget values
XL_models = widget_settings.get('XL_models', False)
inpainting_model = widget_settings.get('inpainting_model', False)
model_selections = widget_settings.get('model', ('none',))
vae_selections = widget_settings.get('vae', ('none',))
lora_selections = widget_settings.get('lora', ('none',))
controlnet_selections = widget_settings.get('controlnet', ('none',))
latest_webui = widget_settings.get('latest_webui', True)
latest_extensions = widget_settings.get('latest_extensions', True)

# --- The rest of the script logic ---
ipyRun = get_ipython().run_line_magic

# Check and install WebUI if it doesn't exist
if not WEBUI_PATH.exists():
    print(f"⌚ Unpacking Stable Diffusion | WEBUI: {UI}...")
    ipyRun('run', f'"{SCRIPTS / "UIs" / UI}.py"')
    handle_setup_timer(str(WEBUI_PATH), env_settings.get('start_timer'))
    print(f"🚀 Unpacking {UI} Complete!")
else:
    print(f"🔧 Current WebUI: {UI} | Already installed.")

# Update logic
if latest_webui or latest_extensions:
    action = 'WebUI and Extensions' if latest_webui and latest_extensions else ('WebUI' if latest_webui else 'Extensions')
    print(f"⌚️ Updating {action}...")
    with capture.capture_output():
        if latest_webui:
            subprocess.run(['git', '-C', str(WEBUI_PATH), 'pull'])
        if latest_extensions:
            for entry in os.listdir(str(extension_dir)):
                dir_path = os.path.join(str(extension_dir), entry)
                if os.path.isdir(dir_path) and os.path.exists(os.path.join(dir_path, '.git')):
                    subprocess.run(['git', '-C', dir_path, 'pull'])
    print(f"✨ Update {action} Complete!")

# Data loading
model_files_path = SCRIPTS / ('_xl-models-data.py' if XL_models else '_models-data.py')
loras_data_path = SCRIPTS / '_loras-data.py'
with open(model_files_path, 'r', encoding='utf-8') as f: exec(f.read(), globals())
with open(loras_data_path, 'r', encoding='utf-8') as f: exec(f.read(), globals())

model_list = globals().get('sdxl_models_data' if XL_models else 'sd15_model_data', {})
vae_list = globals().get('sdxl_vae_data' if XL_models else 'sd15_vae_data', {})
lora_list_to_use = globals().get('lora_data', {}).get('sdxl_loras' if XL_models else 'sd15_loras', {})
controlnet_list_data = globals().get('controlnet_list', {})

# Download logic
def handle_submodels(selections, model_dict, dst_dir, inpainting=False):
    # This function remains the same as the one I provided previously
    download_list = []
    if not isinstance(selections, (list, tuple)): return download_list
    cleaned_selections = [re.sub(r'^\d+\.\s*', '', sel) for sel in selections]
    for selection_name in cleaned_selections:
        if selection_name == 'none': continue
        if selection_name == 'ALL':
            for model_group_key in model_dict:
                model_group_items = model_dict[model_group_key]
                items_to_process = model_group_items if isinstance(model_group_items, list) else [model_group_items]
                for item in items_to_process:
                    name = item.get('name') or os.path.basename(item['url'])
                    if not inpainting and "inpainting" in name.lower():
                        continue
                    download_list.append(f"{item['url']} {dst_dir} {name}")
            continue
        if selection_name in model_dict:
            model_group = model_dict[selection_name]
            items_to_process = model_group if isinstance(model_group, list) else [model_group]
            for model_info in items_to_process:
                name = model_info.get('name') or os.path.basename(model_info['url'])
                if not inpainting and "inpainting" in name.lower():
                    continue
                download_list.append(f"{model_info['url']} {dst_dir} {name}")
    return download_list

# Main execution
print('📦 Processing asset download selections...')
line_entries = []
line_entries.extend(handle_submodels(model_selections, model_list, model_dir, inpainting_model))
line_entries.extend(handle_submodels(vae_selections, vae_list, vae_dir))
line_entries.extend(handle_submodels(lora_selections, lora_list_to_use, lora_dir))
line_entries.extend(handle_submodels(controlnet_selections, controlnet_list_data, control_dir))

download_line = ', '.join(filter(None, line_entries))

if download_line:
    print("Starting asset downloads...")
    m_download(download_line, log=True)
else:
    print("No additional assets selected for download.")

print('\r🏁 Download processing complete!')
ipyRun('run', f'"{SCRIPTS}/download-result.py"')
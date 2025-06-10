# ~ download.py | by ANXETY ~ (Corrected and Complete Version)

from webui_utils import handle_setup_timer
from CivitaiAPI import CivitAiAPI
from Manager import m_download
import json_utils as js

from IPython.display import clear_output
from IPython.utils import capture
from urllib.parse import urlparse
from IPython import get_ipython
from datetime import timedelta
from pathlib import Path
import subprocess
import time
import json
import sys
import re
import os

# --- Setup & Constants ---
DOWNLOADER_VERSION = "2025.06.10.1_complete_patch"
CD = os.chdir
ipyRun = get_ipython().run_line_magic

HOME = Path(js.read(os.path.join(Path.home(), 'ANXETY', 'settings.json'), 'ENVIRONMENT.home_path', str(Path.home())))
SCR_PATH = HOME / 'ANXETY'
SCRIPTS = SCR_PATH / 'scripts'
SETTINGS_PATH = SCR_PATH / 'settings.json'

class COLORS: R,G,Y,B,lB,X = "\033[31m","\033[32m","\033[33m","\033[34m","\033[36;1m","\033[0m"
COL = COLORS

print(f"✨ Downloader Version: {DOWNLOADER_VERSION}")

# --- Load Settings ---
settings = js.read(SETTINGS_PATH)
env_settings = settings.get('ENVIRONMENT', {})
widget_settings = settings.get('WIDGETS', {})
webui_settings = settings.get('WEBUI', {})

# Explicitly load all widget values and paths
XL_models = widget_settings.get('XL_models', False)
inpainting_model = widget_settings.get('inpainting_model', False)
model_selections = widget_settings.get('model', ('none',))
vae_selections = widget_settings.get('vae', ('none',))
lora_selections = widget_settings.get('lora', ('none',))
controlnet_selections = widget_settings.get('controlnet', ('none',))
latest_webui = widget_settings.get('latest_webui', True)
latest_extensions = widget_settings.get('latest_extensions', True)
civitai_token = widget_settings.get('civitai_token', None)

UI = webui_settings.get('current')
WEBUI_PATH = Path(webui_settings.get('webui_path'))
model_dir = Path(webui_settings.get('model_dir'))
vae_dir = Path(webui_settings.get('vae_dir'))
lora_dir = Path(webui_settings.get('lora_dir'))
control_dir = Path(webui_settings.get('control_dir'))
extension_dir = Path(webui_settings.get('extension_dir'))
# Add other necessary directories if they are used later
adetailer_dir = Path(webui_settings.get('adetailer_dir'))
embed_dir = Path(webui_settings.get('embed_dir'))
upscale_dir = Path(webui_settings.get('upscale_dir'))
clip_dir = Path(webui_settings.get('clip_dir', ''))
unet_dir = Path(webui_settings.get('unet_dir', ''))
vision_dir = Path(webui_settings.get('vision_dir', ''))
encoder_dir = Path(webui_settings.get('encoder_dir', ''))
diffusion_dir = Path(webui_settings.get('diffusion_dir', ''))
config_dir = Path(webui_settings.get('config_dir', ''))


# --- WebUI Installation ---
start_timer = env_settings.get('start_timer')

if not WEBUI_PATH.exists():
    start_install = time.time()
    print(f"⌚ Unpacking Stable Diffusion... | WEBUI: {COL.B}{UI}{COL.X}", end='')
    
    # This is the crucial step that was missing
    ipyRun('run', f'"{SCRIPTS / "UIs" / UI}.py"')
    handle_setup_timer(str(WEBUI_PATH), start_timer)

    install_time = time.time() - start_install
    minutes, seconds = divmod(int(install_time), 60)
    print(f"\r🚀 Unpacking {COL.B}{UI}{COL.X} Complete! {minutes:02}:{seconds:02} ⚡" + ' '*25)
else:
    print(f"🔧 Current WebUI: {COL.B}{UI}{COL.X}")
    print('🚀 Unpacking complete. Skipping. ⚡')


# --- Update Logic ---
if latest_webui or latest_extensions:
    action = 'WebUI and Extensions' if latest_webui and latest_extensions else ('WebUI' if latest_webui else 'Extensions')
    print(f"⌚️ Updating {action}...", end='')
    with capture.capture_output():
        subprocess.run(['git', 'config', '--global', 'user.email', 'you@example.com'], capture_output=True)
        subprocess.run(['git', 'config', '--global', 'user.name', 'Your Name'], capture_output=True)
        if latest_webui:
            subprocess.run(['git', '-C', str(WEBUI_PATH), 'pull'], capture_output=True)
        if latest_extensions:
            os.makedirs(extension_dir, exist_ok=True)
            for entry in os.listdir(str(extension_dir)):
                dir_path = os.path.join(str(extension_dir), entry)
                if os.path.isdir(dir_path) and os.path.exists(os.path.join(dir_path, '.git')):
                    subprocess.run(['git', '-C', str(dir_path), 'pull'], capture_output=True)
    print(f"\r✨ Update {action} Complete!")


# --- Data Loading ---
model_files_path = SCRIPTS / ('_xl-models-data.py' if XL_models else '_models-data.py')
with open(model_files_path, 'r', encoding='utf-8') as f: exec(f.read(), globals())

loras_data_path = SCRIPTS / '_loras-data.py'
with open(loras_data_path, 'r', encoding='utf-8') as f: exec(f.read(), globals())

model_list = sdxl_models_data if XL_models else sd15_model_data
vae_list = sdxl_vae_data if XL_models else sd15_vae_data
lora_list_to_use = lora_data.get('sdxl_loras', {}) if XL_models else lora_data.get('sd15_loras', {})


# --- Asset Download Logic ---
def handle_submodels(selections, model_dict, dst_dir, inpainting=False):
    download_list = []
    if not isinstance(selections, (list, tuple)): return download_list
    
    # Remove numbering like "1. " from selection names
    cleaned_selections = [re.sub(r'^\d+\.\s*', '', sel) for sel in selections]
    
    for selection_name in cleaned_selections:
        if selection_name == 'none': continue
        
        # Handle 'ALL' selection
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

        # Handle specific selection
        if selection_name in model_dict:
            model_group = model_dict[selection_name]
            items_to_process = model_group if isinstance(model_group, list) else [model_group]
            
            for model_info in items_to_process:
                name = model_info.get('name') or os.path.basename(model_info['url'])
                if not inpainting and "inpainting" in name.lower():
                    continue
                download_list.append(f"{model_info['url']} {dst_dir} {name}")
    return download_list


# --- Main Execution for Asset Downloads ---
print('📦 Processing asset download selections...')
line_entries = []
line_entries.extend(handle_submodels(model_selections, model_list, model_dir, inpainting_model))
line_entries.extend(handle_submodels(vae_selections, vae_list, vae_dir))
line_entries.extend(handle_submodels(lora_selections, lora_list_to_use, lora_dir))
line_entries.extend(handle_submodels(controlnet_selections, globals().get('controlnet_list', {}), control_dir))

download_line = ', '.join(filter(None, line_entries))

if download_line:
    print("Starting asset downloads...")
    m_download(download_line, log=True)
else:
    print("No additional assets selected for download.")

print('\r🏁 Download processing complete!')

# --- Display Results ---
ipyRun('run', f'"{SCRIPTS}/download-result.py"')
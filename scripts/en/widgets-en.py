# ~ widgets.py | by ANXETY ~ (Final Path Correction)

import ipywidgets as widgets
from pathlib import Path
import os
import sys

# --- Get the correct paths from settings.json ---
# This is the single source of truth written by setup.py
# We add the modules path first so we can import json_utils
anxety_path = Path.home() / 'ANXETY'
modules_path = anxety_path / 'modules'
if str(modules_path) not in sys.path:
    sys.path.insert(0, str(modules_path))

import json_utils as js
from webui_utils import update_current_webui
from widget_factory import WidgetFactory

# Load all paths from the settings file created by setup.py
settings_path = anxety_path / 'settings.json'
SCRIPTS = Path(js.read(settings_path, 'ENVIRONMENT.scr_path')) / 'scripts'
CSS = SCRIPTS.parent / 'CSS'
JS = SCRIPTS.parent / 'JS'
ENV_NAME = js.read(settings_path, 'ENVIRONMENT.env_name')

widgets_css = CSS / 'main-widgets.css'
widgets_js = JS / 'main-widgets.js'

## ======================= WIDGETS =======================

factory = WidgetFactory()
factory.load_css(widgets_css)
factory.load_js(widgets_js)
HR = widgets.HTML('<hr>')

def read_model_data(file_path, data_key_in_file, prefixes=['none']):
    """Reads data from a file, extracts a dictionary, and returns a numbered list of its keys."""
    local_vars = {}
    if not file_path.exists():
        print(f"Warning: Data file not found at {file_path}. Skipping.")
        return prefixes
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            exec(f.read(), {}, local_vars)
        except Exception as e:
            print(f"Error executing data file {file_path}: {e}")
            return prefixes
    
    data_dict = local_vars
    for key_part in data_key_in_file.split('.'):
        data_dict = data_dict.get(key_part, {})
        if not isinstance(data_dict, dict):
            return prefixes
    
    names = list(data_dict.keys())
    numbered_names = [f"{i+1}. {name}" for i, name in enumerate(names)]
    return prefixes + numbered_names

webui_selection = {
    'A1111': "--xformers --no-half-vae", 'ComfyUI': "--use-sage-attention --dont-print-server",
    'Forge': "--disable-xformers --opt-sdp-attention --cuda-stream --pin-shared-memory",
    'Classic': "--persistent-patches --cuda-stream --pin-shared-memory",
    'ReForge': "--xformers --cuda-stream --pin-shared-memory", 'SD-UX': "--xformers --no-half-vae"
}

# Data file paths
sd15_models_path = SCRIPTS / '_models-data.py'
sdxl_models_path = SCRIPTS / '_xl-models-data.py'
loras_data_path = SCRIPTS / '_loras-data.py'

# --- MODEL ---
model_header = factory.create_header('Model Selection (Ctrl+Click for multiple)')
model_options = read_model_data(sd15_models_path, 'sd15_model_data')
model_widget = factory.create_select_multiple(model_options, 'Models:', ('none',))
inpainting_model_widget = factory.create_checkbox('Inpainting Models', False, ['inpaint'], layout={'width': 'auto'})
XL_models_widget = factory.create_checkbox('SDXL', False, ['sdxl'], layout={'width': 'auto'})
switch_model_widget = factory.create_hbox([inpainting_model_widget, XL_models_widget])

# --- VAE ---
vae_header = factory.create_header('VAE Selection')
vae_options = read_model_data(sd15_models_path, 'sd15_vae_data', ['none', 'ALL'])
vae_widget = factory.create_select_multiple(vae_options, 'VAEs:', ('none',))

# --- LoRA ---
lora_header = factory.create_header('LoRA Selection')
lora_options = read_model_data(loras_data_path, 'lora_data.sd15_loras', ['none', 'ALL'])
lora_widget = factory.create_select_multiple(lora_options, 'LoRAs:', ('none',))

# --- ControlNet ---
controlnet_header = factory.create_header('ControlNet Selection')
controlnet_options = read_model_data(sd15_models_path, 'controlnet_list', ['none', 'ALL'])
controlnet_widget = factory.create_select_multiple(controlnet_options, 'ControlNets:', ('none',))

# --- Additional ---
additional_header = factory.create_header('Additional Settings')
latest_webui_widget = factory.create_checkbox('Update WebUI', True)
latest_extensions_widget = factory.create_checkbox('Update Extensions', True)
change_webui_widget = factory.create_dropdown(list(webui_selection.keys()), 'WebUI:', 'Forge', layout={'width': 'auto'})
commandline_arguments_widget = factory.create_text('Arguments:', webui_selection.get('Forge', ''))

save_button = factory.create_button('Save & Close', ['button', 'button_save'])
GDrive_button = factory.create_button('', layout={'width': '48px', 'height': '48px'}, class_names=['gdrive-btn'])
if ENV_NAME != 'Google Colab': GDrive_button.layout.display = 'none'

# --- Layout Assembly ---
model_col = factory.create_vbox([model_header, model_widget, switch_model_widget])
vae_col = factory.create_vbox([vae_header, vae_widget])
lora_col = factory.create_vbox([lora_header, lora_widget])
cnet_col = factory.create_vbox([controlnet_header, controlnet_widget])
download_box = factory.create_vbox([model_col, vae_col, lora_col, cnet_col], class_names=['container'])
additional_box = factory.create_vbox([additional_header, factory.create_hbox([latest_webui_widget, latest_extensions_widget, change_webui_widget]), commandline_arguments_widget], class_names=['container'])
WIDGET_LIST = factory.create_vbox([factory.create_hbox([download_box, GDrive_button]), additional_box, save_button], class_names=['mainContainer'])
factory.display(WIDGET_LIST)

# --- Callbacks ---
def on_xl_toggle(change):
    is_xl = change.new
    model_path = sdxl_models_path if is_xl else sd15_models_path
    model_key = 'sdxl_models_data' if is_xl else 'sd15_model_data'
    vae_key = 'sdxl_vae_data' if is_xl else 'sd15_vae_data'
    lora_key = 'lora_data.sdxl_loras' if is_xl else 'lora_data.sd15_loras'
    cnet_key = 'controlnet_list' # controlnet_list is the same key in both files
    
    model_widget.options = read_model_data(model_path, model_key)
    vae_widget.options = read_model_data(model_path, vae_key, ['none', 'ALL'])
    lora_widget.options = read_model_data(loras_data_path, lora_key, ['none', 'ALL'])
    controlnet_widget.options = read_model_data(model_path, cnet_key, ['none', 'ALL'])
    
    model_widget.value, vae_widget.value, lora_widget.value, controlnet_widget.value = ('none',), ('none',), ('none',), ('none',)

def on_webui_change(change):
    commandline_arguments_widget.value = webui_selection.get(change.new, '')

# --- Settings and Event Handling ---
SETTINGS_KEYS = [
    'XL_models', 'model', 'inpainting_model', 'vae', 'lora', 'controlnet',
    'latest_webui', 'latest_extensions', 'change_webui', 'commandline_arguments'
]
def save_settings():
    widget_values = {}
    for key in SETTINGS_KEYS:
        widget_name = f"{key}_widget"
        if widget_name in globals():
            widget_values[key] = globals()[widget_name].value
    js.save(settings_path, 'WIDGETS', widget_values)
    js.save(settings_path, 'mountGDrive', getattr(GDrive_button, 'toggle', False))
    update_current_webui(change_webui_widget.value)

def load_settings():
    if js.key_exists(settings_path, 'WIDGETS'):
        widget_data = js.read(settings_path, 'WIDGETS')
        for key in SETTINGS_KEYS:
            if key in widget_data and f"{key}_widget" in globals():
                globals()[f"{key}_widget"].value = widget_data.get(key, ('none',))
    if ENV_NAME == 'Google Colab':
        GDrive_button.toggle = js.read(settings_path, 'mountGDrive', False)
        GDrive_button.add_class('active') if GDrive_button.toggle else GDrive_button.remove_class('active')

def on_save_click(b):
    save_settings()
    factory.close([WIDGET_LIST], ['hide'], delay=0.8)

# --- Initialisation ---
XL_models_widget.observe(on_xl_toggle, 'value')
change_webui_widget.observe(on_webui_change, 'value')
save_button.on_click(on_save_click)
load_settings()
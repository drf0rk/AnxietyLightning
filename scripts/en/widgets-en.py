# ~ widgets.py | by ANXETY ~ (All-in-One Fix)

from widget_factory import WidgetFactory
from webui_utils import update_current_webui
import json_utils as js
import ipywidgets as widgets
from pathlib import Path
import os
import re

# --- Constants and Platform-Aware Pathing ---
# This block robustly finds the project root directory
cwd = Path.cwd()
project_dir_name = 'ANXETY'
if cwd.name == project_dir_name:
    ANXETY_ROOT = cwd
else:
    ANXETY_ROOT = cwd / project_dir_name

if not ANXETY_ROOT.is_dir():
    raise FileNotFoundError(f"FATAL: Could not find project root at '{ANXETY_ROOT}'")

# Use the robust ANXETY_ROOT to define all other paths
SETTINGS_PATH = ANXETY_ROOT / 'settings.json'
SCRIPTS = ANXETY_ROOT / 'scripts'
CSS = ANXETY_ROOT / 'CSS'
JS = ANXETY_ROOT / 'JS'
widgets_css = CSS / 'main-widgets.css'
widgets_js = JS / 'main-widgets.js'
ENV_NAME = js.read(str(SETTINGS_PATH), 'ENVIRONMENT.env_name', 'local')


# --- Helper Functions ---
factory = WidgetFactory()

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

    data_dict = local_vars.get(data_key_in_file, {})
    if not isinstance(data_dict, dict):
        print(f"Warning: Key '{data_key_in_file}' in {file_path} is not a dictionary.")
        return prefixes
        
    return prefixes + [f"{i+1}. {name}" for i, name in enumerate(data_dict.keys())]

# --- Widget Creation ---
# Models
model_list = read_model_data(SCRIPTS / '_models-data.py', 'sd15_model_data')
XL_model_list = read_model_data(SCRIPTS / '_xl-models-data.py', 'sdxl_models_data')
# VAEs
vae_list = read_model_data(SCRIPTS / '_models-data.py', 'sd15_vae_data', ['none', 'ALL'])
XL_vae_list = read_model_data(SCRIPTS / '_xl-models-data.py', 'sdxl_vae_data', ['none', 'ALL'])
# ControlNets
cnet_list = read_model_data(SCRIPTS / '_models-data.py', 'controlnet_list', ['none', 'ALL'])
XL_cnet_list = read_model_data(SCRIPTS / '_xl-models-data.py', 'controlnet_list', ['none', 'ALL'])

# Main Widgets
XL_models_widget = factory.create_checkbox(description='XL', value=False, class_names='sdxl')
model_widget = factory.create_dropdown(description='Models:', options=model_list)
inpainting_model_widget = factory.create_checkbox(description='Inpainting', value=False, class_names='inpaint')
vae_widget = factory.create_dropdown(description='VAE:', options=vae_list)
lora_widget = factory.create_textarea(description='LoRA:', placeholder='Enter LoRA URLs, one per line')
embedding_widget = factory.create_textarea(description='Embeddings:', placeholder='Enter Embedding URLs, one per line')
controlnet_widget = factory.create_select_multiple(description='ControlNet:', options=cnet_list)

# WebUI Widgets
webui_selection = {'A1111': '', 'Forge': '', 'ComfyUI': ''}
latest_webui_widget = factory.create_checkbox('Update WebUI', False)
latest_extensions_widget = factory.create_checkbox('Update Extensions', False)
change_webui_widget = factory.create_dropdown('WebUI:', ['A1111', 'Forge', 'ComfyUI'])
commandline_arguments_widget = factory.create_text('Arguments:', '')

# Download Manager
Model_url_widget = factory.create_text('Model:', 'Model URL')
Vae_url_widget = factory.create_text('VAE:', 'VAE URL')
LoRA_url_widget = factory.create_text('LoRA:', 'LoRA URL')
Embedding_url_widget = factory.create_text('Embedding:', 'Embedding URL')
Extensions_url_widget = factory.create_text('Extensions:', 'Extension Git-Repo')
ADetailer_url_widget = factory.create_text('ADetailer:', 'ADetailer URL')
custom_file_urls_widget = factory.create_textarea('Custom Files:', 'Enter URLs, one per line')
download_manager_widget = factory.create_checkbox('Download Manager', True)
empowerment_widget = factory.create_html('<a href="https://github.com/d-fa/empowerment" target="_blank">Empowerment Mode</a>')

# Buttons
GDrive_button = factory.create_button(description='Mount GDrive', class_names='gdrive-btn')
save_button = factory.create_button(description='Save settings', class_names='button_save')

# --- Callbacks and Observers ---
def on_xl_change(change):
    is_xl = change.new
    model_widget.options = XL_model_list if is_xl else model_list
    vae_widget.options = XL_vae_list if is_xl else vae_list
    controlnet_widget.options = XL_cnet_list if is_xl else cnet_list

def on_webui_change(change):
    commandline_arguments_widget.value = webui_selection.get(change.new, '')

# --- Settings Save/Load ---
SETTINGS_KEYS = [
    'XL_models', 'model', 'inpainting_model', 'vae', 'lora', 'controlnet',
    'latest_webui', 'latest_extensions', 'change_webui', 'commandline_arguments',
    'Model_url', 'Vae_url', 'LoRA_url', 'Embedding_url', 'Extensions_url', 'ADetailer_url',
    'custom_file_urls'
]
def save_settings():
    widget_values = {}
    for key in SETTINGS_KEYS:
        widget_name = f"{key}_widget"
        if widget_name in globals():
            widget_values[key] = globals()[widget_name].value
    js.save(str(SETTINGS_PATH), 'WIDGETS', widget_values)
    js.save(str(SETTINGS_PATH), 'mountGDrive', getattr(GDrive_button, 'toggle', False))
    update_current_webui(change_webui_widget.value)

def load_settings():
    if js.key_exists(str(SETTINGS_PATH), 'WIDGETS'):
        widget_data = js.read(str(SETTINGS_PATH), 'WIDGETS')
        for key in SETTINGS_KEYS:
            if key in widget_data and f"{key}_widget" in globals():
                globals()[f"{key}_widget"].value = widget_data.get(key)
    GDrive_button.toggle = js.read(str(SETTINGS_PATH), 'mountGDrive', False)
    GDrive_button.add_class('active') if GDrive_button.toggle else GDrive_button.remove_class('active')

def on_save_click(button):
    save_settings()

# --- Display Logic ---
factory.load_css(widgets_css)

# Connect observers
XL_models_widget.observe(on_xl_change, names='value')
change_webui_widget.observe(on_webui_change, names='value')
save_button.on_click(on_save_click)

# Assemble UI components
webui_box = factory.create_vbox([change_webui_widget, commandline_arguments_widget, factory.create_hbox([latest_webui_widget, latest_extensions_widget])], 'box_webui')
settings_box = factory.create_vbox([factory.create_html('Settings', 'header'), factory.create_hbox([XL_models_widget, inpainting_model_widget])], 'box_settings')
top_container = factory.create_hbox([webui_box, settings_box], 'container_webui')

models_container = factory.create_vbox([model_widget, vae_widget, lora_widget, embedding_widget, controlnet_widget], 'container_models')

download_box = factory.create_vbox([factory.create_html('Download Manager', 'header'), factory.create_hbox([download_manager_widget, empowerment_widget]), Model_url_widget, Vae_url_widget, LoRA_url_widget, Embedding_url_widget, Extensions_url_widget, ADetailer_url_widget], 'box_download')
custom_files_box = factory.create_vbox([factory.create_html('Custom files', 'header'), custom_file_urls_widget], 'box_download')
download_container = factory.create_hbox([download_box, custom_files_box], 'container_cdl')

# Display everything
display(top_container, models_container, download_container, GDrive_button, save_button)

# Load settings and JS
load_settings()
js_content = ""
if widgets_js.exists():
    with open(widgets_js, 'r', encoding='utf-8') as f:
        js_content = f.read()
display(HTML(f"<script>{js_content}</script>"))
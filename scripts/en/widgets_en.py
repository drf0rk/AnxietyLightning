# /content/ANXETY/scripts/en/widgets_en.py (v14 - Token Persistence Update)

import ipywidgets as widgets
from IPython.display import display, clear_output, HTML
from pathlib import Path
import sys
import os
import runpy
import subprocess
import json
import time
from IPython import get_ipython

# --- Pathing & Imports ---
ANXETY_ROOT = Path('/content/ANXETY')
if str(ANXETY_ROOT) not in sys.path: sys.path.insert(0, str(ANXETY_ROOT))
if str(ANXETY_ROOT / 'modules') not in sys.path: sys.path.insert(0, str(ANXETY_ROOT / 'modules'))

from modules.widget_factory import WidgetFactory
from modules.webui_utils import update_current_webui, WEBUI_PATHS, DEFAULT_UI
from modules.Manager import m_clone
import modules.json_utils as js

# --- Main UI Class ---
class AnxietyUI:
    def __init__(self):
        self.factory = WidgetFactory()
        self.widgets = {}
        self.layouts = {}
        self.buttons = {}
        self.webui_selection_args = {
            'A1111': "--xformers --no-half-vae --enable-insecure-extension-access --disable-console-progressbars --theme dark",
            'ComfyUI': "--use-sage-attention --dont-print-server",
            'Forge': "--disable-xformers --opt-sdp-attention --cuda-stream --pin-shared-memory --enable-insecure-extension-access --disable-console-progressbars --theme dark",
            'Classic': "--persistent-patches --cuda-stream --pin-shared-memory --enable-insecure-extension-access --disable-console-progressbars --theme dark",
            'ReForge': "--xformers --cuda-stream --pin-shared-memory --enable-insecure-extension-access --disable-console-progressbars --theme dark",
            'SD-UX': "--xformers --no-half-vae --enable-insecure-extension-access --disable-console-progressbars --theme dark"
        }
        self.factory.load_css(ANXETY_ROOT / 'CSS' / 'main-widgets.css')

    def create_ui(self):
        self._create_widgets()
        self._create_layouts()
        self._assign_callbacks()
        self._update_model_lists()
        self._update_args_from_webui()
        display(self.layouts['main_container'])

    def _create_widgets(self):
        self.widgets['sdxl_toggle'] = self.factory.create_toggle_button(description="SDXL Models", value=False, button_style='info', tooltip='Toggle SDXL Models', icon='rocket')
        self.widgets['detailed_download'] = self.factory.create_checkbox(description="Detailed download")
        webui_options = ['ReForge', 'Forge', 'A1111', 'ComfyUI', 'Classic', 'SD-UX']
        self.widgets['change_webui'] = self.factory.create_dropdown('WebUI:', webui_options, 'ReForge')
        self.widgets['commandline_arguments'] = self.factory.create_text(description="Arguments:")
        
        # --- CHANGE: Ngrok Token Widget has been removed from the UI ---
        # It is now handled by the bootstrap cell for persistence.
        
        self.widgets['model_list'], self.widgets['vae_list'], self.widgets['controlnet_list'], self.widgets['lora_list'] = [], [], [], []
        self.widgets['extension_url_input'] = self.factory.create_text("", placeholder="Paste Git Repo URL for Extension...")
        self.buttons['install_extension'] = self.factory.create_button("+", tooltip="Install this extension now")
        self.buttons['install_extension'].layout.width = '40px'
        self.widgets['embedding_url'] = self.factory.create_textarea("", placeholder="Paste Embedding URLs here, one per line...")
        self.widgets['extra_files_url'] = self.factory.create_textarea("", placeholder="Paste any other direct download URLs here...")

    def _create_layouts(self):
        self.layouts['models_box'] = widgets.VBox(self.widgets['model_list'])
        self.layouts['vaes_box'] = widgets.VBox(self.widgets['vae_list'])
        self.layouts['cnets_box'] = widgets.VBox(self.widgets['controlnet_list'])
        self.layouts['loras_box'] = widgets.VBox(self.widgets['lora_list'])
        extension_installer_box = widgets.HBox([self.widgets['extension_url_input'], self.buttons['install_extension']], layout={'width': '100%'})
        self.widgets['extension_url_input'].layout.width = '95%'

        # --- CHANGE: Removed Ngrok widget from the Accordion ---
        accordion = widgets.Accordion(children=[
            self.layouts['models_box'], self.layouts['vaes_box'], self.layouts['cnets_box'], self.layouts['loras_box'], 
            self.widgets['embedding_url'], extension_installer_box, self.widgets['extra_files_url']
        ])
        titles = ['Checkpoints', 'VAEs', 'ControlNets', 'LoRAs', 'Embeddings (URL)', 'Install Extension (Git)', 'Extra Files (URL)']
        for i, title in enumerate(titles): accordion.set_title(i, title)
        
        self.buttons['launch'] = self.factory.create_button(description="Install, Download & Launch", class_names=['button', 'button_save'], icon='paper-plane')
        top_bar = widgets.HBox([self.widgets['change_webui'], self.widgets['sdxl_toggle'], self.widgets['detailed_download']])
        self.layouts['output_layout'] = widgets.Output()
        self.layouts['main_container'] = widgets.VBox([top_bar, self.widgets['commandline_arguments'], accordion, self.buttons['launch'], self.layouts['output_layout']])

    def _assign_callbacks(self):
        self.widgets['sdxl_toggle'].observe(self._on_sdxl_toggled, names='value')
        self.widgets['change_webui'].observe(self._on_webui_changed, names='value')
        self.buttons['install_extension'].on_click(self._on_install_extension_clicked)
        self.buttons['launch'].on_click(self.on_launch_click)

    def _on_sdxl_toggled(self, change): self._update_model_lists()
    def _on_webui_changed(self, change): self._update_args_from_webui()
        
    def _on_install_extension_clicked(self, b):
        pass

    def _update_args_from_webui(self):
        selected_ui = self.widgets['change_webui'].value
        self.widgets['commandline_arguments'].value = self.webui_selection_args.get(selected_ui, "")

    def _update_model_lists(self):
        is_xl = self.widgets['sdxl_toggle'].value
        models_py_path = ANXETY_ROOT / 'scripts' / ('_xl-models-data.py' if is_xl else '_models-data.py')
        loras_py_path = ANXETY_ROOT / 'scripts' / '_loras-data.py'
        models_data = runpy.run_path(str(models_py_path))
        loras_data = runpy.run_path(str(loras_py_path))
        model_dict = models_data.get('sdxl_models_data' if is_xl else 'sd15_model_data', {})
        vae_dict = models_data.get('sdxl_vae_data' if is_xl else 'sd15_vae_data', {})
        cnet_dict = models_data.get('controlnet_list', {})
        lora_dict = loras_data.get('lora_data', {}).get('sdxl_loras' if is_xl else 'sd15_loras', {})
        self.widgets['model_list'] = [self.factory.create_checkbox(description=name) for name in model_dict.keys()]
        self.widgets['vae_list'] = [self.factory.create_checkbox(description=name) for name in vae_dict.keys()]
        self.widgets['controlnet_list'] = [self.factory.create_checkbox(description=name) for name in cnet_dict.keys()]
        self.widgets['lora_list'] = [self.factory.create_checkbox(description=name) for name in lora_dict.keys()]
        self.layouts['models_box'].children = tuple(self.widgets['model_list'])
        self.layouts['vaes_box'].children = tuple(self.widgets['vae_list'])
        self.layouts['cnets_box'].children = tuple(self.widgets['controlnet_list'])
        self.layouts['loras_box'].children = tuple(self.widgets['lora_list'])
        
    def on_launch_click(self, b):
        b.description = "Processing..."; b.icon = "spinner"; b.disabled = True
        with self.layouts['output_layout']:
            clear_output(wait=True)
            self._run_full_sequence()
        b.description = "Launch Complete"; b.icon = "check"; b.disabled = False
        
    def _run_full_sequence(self):
        print("--- 1. Saving All UI Settings ---")
        self.save_settings()
        print("\n--- 2. Running Environment Setup (VENV & Assets) ---")
        get_ipython().run_line_magic('run', str(ANXETY_ROOT / 'scripts' / 'en' / 'downloading-en.py'))
        print("\n--- 3. Launching WebUI ---")
        get_ipython().run_line_magic('run', str(ANXETY_ROOT / 'scripts' / 'launch.py'))
        
    def save_settings(self):
        SETTINGS_PATH = str(ANXETY_ROOT / 'settings.json')
        
        # --- CHANGE: Logic updated to merge settings instead of overwriting ---
        
        # 1. Gather the current UI's widget values (Ngrok token is no longer here)
        current_ui_values = {k: v.value for k, v in self.widgets.items() if hasattr(v, 'value') and not isinstance(v, list)}
        for key in ['model_list', 'vae_list', 'controlnet_list', 'lora_list']:
            if key in self.widgets:
                current_ui_values[key] = [cb.description for cb in self.widgets[key] if cb.value]

        # 2. Read existing WIDGETS data (which includes the token from the bootstrap cell)
        existing_widgets_data = js.read(SETTINGS_PATH, 'WIDGETS', {})

        # 3. Merge the new UI values into the existing data, preserving the token
        existing_widgets_data.update(current_ui_values)

        # 4. Save the merged dictionary back to the WIDGETS key
        js.save(SETTINGS_PATH, 'WIDGETS', existing_widgets_data)
        
        # 5. Save other essential non-widget settings
        js.save(SETTINGS_PATH, 'ENVIRONMENT.home_path', '/content')
        update_current_webui(current_ui_values.get('change_webui'))
        
        print("✅ Configuration saved to settings.json")

if __name__ == "__main__":
    ui = AnxietyUI()
    ui.create_ui()

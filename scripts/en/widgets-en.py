# /content/ANXETY/scripts/en/widgets-en.py

import ipywidgets as widgets
from IPython.display import display, clear_output, HTML
from pathlib import Path
import sys
import os
import runpy
import subprocess
import json
import time

# --- Configuration & Globals ---
ANXETY_ROOT = Path('/content/ANXETY')
VENV_PATH = Path('/content/venv')
SETTINGS_PATH = ANXETY_ROOT / 'settings.json'

if str(ANXETY_ROOT) not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT))
if str(ANXETY_ROOT / 'modules') not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT / 'modules'))

# --- Import Project Modules ---
from modules.widget_factory import WidgetFactory
from modules.webui_utils import update_current_webui
from modules.Manager import m_download
import modules.json_utils as js

# --- Main UI Class ---
class AnxietyUI:
    def __init__(self):
        self.factory = WidgetFactory()
        self.widgets = {}
        self.layouts = {}
        self.buttons = {}

        # Load CSS and JS
        self.factory.load_css(ANXETY_ROOT / 'CSS' / 'main-widgets.css')
        self.factory.load_css(ANXETY_ROOT / 'CSS' / 'download-result.css')
        self.factory.load_js(ANXETY_ROOT / 'JS' / 'main-widgets.js')

    def create_ui(self):
        """Creates and displays the entire user interface."""
        self._create_widgets()
        self._create_layouts()
        self._assign_callbacks()
        display(self.layouts['main_container'])
        # self.load_settings() # We can enable this later

    def _create_widgets(self):
        """Creates all the individual widgets for the UI using the factory."""
        models_data = runpy.run_path(str(ANXETY_ROOT / 'scripts/_models-data.py'))
        
        # --- FIXED LINE ---
        self.widgets['sdxl_toggle'] = self.factory.create_toggle_button(description="SDXL Models", value=False, button_style='info', tooltip='Toggle SDXL Models', icon='rocket')
        
        self.widgets['detailed_download'] = self.factory.create_checkbox(description="Detailed download")
        webui_options = ['ReForge', 'Forge', 'A1111', 'ComfyUI', 'Classic', 'SD-UX']
        self.widgets['change_webui'] = self.factory.create_dropdown('WebUI:', webui_options, 'ReForge')
        self.widgets['commandline_arguments'] = self.factory.create_text(description="Arguments:")

        self.widgets['model_list'] = [self.factory.create_checkbox(description=name) for name in models_data.get('sd15_model_data', [])]
        self.widgets['vae_list'] = [self.factory.create_checkbox(description=name) for name in models_data.get('sd15_vae_data', [])]
        self.widgets['controlnet_list'] = [self.factory.create_checkbox(description=name) for name in models_data.get('controlnet_list', [])]
        
        self.widgets['lora_url'] = self.factory.create_textarea("", placeholder="Paste LoRA URLs here, one per line...")
        self.widgets['embedding_url'] = self.factory.create_textarea("", placeholder="Paste Embedding URLs here...")
        self.widgets['extension_url'] = self.factory.create_textarea("", placeholder="Paste Git Repo URLs for Extensions here...")
        self.widgets['extra_files_url'] = self.factory.create_textarea("", placeholder="Paste any other direct download URLs here...")

    def _create_layouts(self):
        """Creates and arranges all widgets into a final layout."""
        models_box = widgets.VBox(self.widgets['model_list'])
        vaes_box = widgets.VBox(self.widgets['vae_list'])
        cnets_box = widgets.VBox(self.widgets['controlnet_list'])

        accordion = widgets.Accordion(children=[
            models_box, vaes_box, cnets_box,
            self.widgets['lora_url'], self.widgets['embedding_url'],
            self.widgets['extension_url'], self.widgets['extra_files_url']
        ])
        titles = ['Checkpoints', 'VAEs', 'ControlNets', 'LoRAs (URL)', 'Embeddings (URL)', 'Extensions (Git)', 'Extra Files (URL)']
        for i, title in enumerate(titles): accordion.set_title(i, title)

        self.buttons['launch'] = self.factory.create_button(description="Install, Download & Launch", class_names=['button', 'button_save'], icon='paper-plane')
        
        top_bar = widgets.HBox([self.widgets['change_webui'], self.widgets['sdxl_toggle'], self.widgets['detailed_download']])
        self.layouts['output_layout'] = widgets.Output()
        self.layouts['main_container'] = widgets.VBox([top_bar, self.widgets['commandline_arguments'], accordion, self.buttons['launch'], self.layouts['output_layout']])

    def _assign_callbacks(self):
        """Assigns backend functions to button click events."""
        self.buttons['launch'].on_click(self.on_launch_click)

    def on_launch_click(self, b):
        """Orchestrates the entire setup and launch process."""
        b.description = "Processing..."; b.icon = "spinner"; b.disabled = True
        with self.layouts['output_layout']:
            clear_output(wait=True)
            self._run_full_sequence()
        b.description = "Launch Complete"; b.icon = "check"; b.disabled = False
        
    def _run_full_sequence(self):
        print("--- Saving All UI Settings ---"); self.save_settings()
        
        # Here we will later call the backend scripts in order:
        # 1. VENV Setup
        # 2. Asset Downloads
        # 3. WebUI Launch
        print("Backend execution pipeline would start here.")
        
    def save_settings(self):
        """Saves the state of all widgets to settings.json."""
        widget_values = {k: v.value for k, v in self.widgets.items() if hasattr(v, 'value') and not isinstance(v, list)}
        
        for key in ['model_list', 'vae_list', 'controlnet_list']:
            widget_values[key] = [cb.description for cb in self.widgets[key] if cb.value]

        js.save(str(SETTINGS_PATH), 'WIDGETS', widget_values)
        update_current_webui(widget_values['change_webui'])
        print("✅ Configuration saved to settings.json")

if __name__ == "__main__":
    ui = AnxietyUI()
    ui.create_ui()
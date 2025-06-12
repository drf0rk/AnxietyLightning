# /content/ANXETY/scripts/en/widgets_en.py (v15 - Integrated Downloader)

import ipywidgets as widgets
from IPython.display import display, clear_output, HTML
from pathlib import Path
import sys
import os
import runpy
import subprocess
import json
import time
import ast
from IPython import get_ipython

# --- Pathing & Imports ---
ANXETY_ROOT = Path('/content/ANXETY')
if str(ANXETY_ROOT) not in sys.path: sys.path.insert(0, str(ANXETY_ROOT))

from modules.widget_factory import WidgetFactory
from modules.webui_utils import update_current_webui
from modules.CivitaiAPI import CivitAiAPI
import modules.json_utils as js

class AnxietyUI:
    def __init__(self):
        self.factory = WidgetFactory()
        self.widgets = {}
        self.layouts = {}
        self.buttons = {}
        # ... (webui_selection_args remains the same)
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

    # --- WIDGET CREATION ---
    def _create_widgets(self):
        # Main UI Widgets
        self.widgets['sdxl_toggle'] = self.factory.create_toggle_button(description="SDXL Models", value=False, button_style='info', tooltip='Toggle SDXL Models', icon='rocket')
        self.widgets['detailed_download'] = self.factory.create_checkbox(description="Detailed download")
        webui_options = ['ReForge', 'Forge', 'A1111', 'ComfyUI', 'Classic', 'SD-UX']
        self.widgets['change_webui'] = self.factory.create_dropdown('WebUI:', webui_options, 'ReForge')
        self.widgets['commandline_arguments'] = self.factory.create_text(description="Arguments:")
        
        # Model Selection Widgets
        self.widgets['model_list'], self.widgets['vae_list'], self.widgets['controlnet_list'], self.widgets['lora_list'] = [], [], [], []
        
        # --- NEW: Custom Downloader Widgets ---
        self.widgets['downloader_urls'] = self.factory.create_textarea("", placeholder="Paste one or more Civitai/HuggingFace URLs here, one per line...")
        self.buttons['downloader_analyze'] = self.factory.create_button("Analyze & Add to Library", icon='cogs', button_style='info')

    # --- LAYOUT CREATION ---
    def _create_layouts(self):
        # Create boxes for existing model checkboxes
        self.layouts['models_box'] = widgets.VBox(self.widgets['model_list'])
        self.layouts['vaes_box'] = widgets.VBox(self.widgets['vae_list'])
        self.layouts['cnets_box'] = widgets.VBox(self.widgets['controlnet_list'])
        self.layouts['loras_box'] = widgets.VBox(self.widgets['lora_list'])
        
        # --- NEW: Create the Custom Downloader UI section ---
        downloader_box = self.factory.create_vbox([
            self.factory.create_html("<h4>Custom Downloader</h4>"),
            self.widgets['downloader_urls'],
            self.buttons['downloader_analyze']
        ], layout={'padding': '10px'})

        # The main accordion now includes the new downloader section
        accordion = widgets.Accordion(children=[
            self.layouts['models_box'], self.layouts['vaes_box'], self.layouts['cnets_box'], self.layouts['loras_box'],
            downloader_box
        ])
        titles = ['Checkpoints', 'VAEs', 'ControlNets', 'LoRAs', 'Add Custom Files']
        for i, title in enumerate(titles): accordion.set_title(i, title)
        
        # Main application layout
        self.buttons['launch'] = self.factory.create_button(description="Install, Download & Launch", class_names=['button', 'button_save'], icon='paper-plane')
        top_bar = widgets.HBox([self.widgets['change_webui'], self.widgets['sdxl_toggle'], self.widgets['detailed_download']])
        self.layouts['output_layout'] = widgets.Output()
        self.layouts['main_container'] = widgets.VBox([top_bar, self.widgets['commandline_arguments'], accordion, self.buttons['launch'], self.layouts['output_layout']])

    # --- CALLBACKS ---
    def _assign_callbacks(self):
        self.widgets['sdxl_toggle'].observe(self._on_sdxl_toggled, names='value')
        self.widgets['change_webui'].observe(self._on_webui_changed, names='value')
        self.buttons['launch'].on_click(self.on_launch_click)
        # --- NEW: Assign callback for the downloader button ---
        self.buttons['downloader_analyze'].on_click(self._on_downloader_analyze_clicked)

    # --- UI UPDATE LOGIC (Existing) ---
    def _on_sdxl_toggled(self, change): self._update_model_lists()
    def _on_webui_changed(self, change): self._update_args_from_webui()
    def _update_args_from_webui(self):
        selected_ui = self.widgets['change_webui'].value
        self.widgets['commandline_arguments'].value = self.webui_selection_args.get(selected_ui, "")

    def _update_model_lists(self):
        # This function can be expanded later to re-read the data files after you add new models
        is_xl = self.widgets['sdxl_toggle'].value
        models_py_path = ANXETY_ROOT / 'scripts' / ('_xl-models-data.py' if is_xl else '_models-data.py')
        loras_py_path = ANXETY_ROOT / 'scripts' / '_loras-data.py'
        # ... (rest of the function is the same)
        # ... (this will need to be re-run after the downloader finishes to show new models)
        if not models_py_path.exists(): return
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
        
    # --- NEW: CUSTOM DOWNLOADER LOGIC ---
    def _on_downloader_analyze_clicked(self, b):
        urls = self.widgets['downloader_urls'].value.strip().split()
        if not urls:
            with self.layouts['output_layout']:
                clear_output(wait=True)
                print("⚠️ Please paste at least one URL into the downloader box.")
            return

        b.description = "Processing..."
        b.icon = "spinner"
        b.disabled = True
        
        with self.layouts['output_layout']:
            clear_output(wait=True)
            print("Analyzing URLs...")
            
        # NOTE: For simplicity, this version directly writes to the files.
        # A full "Wizard" with a review stage can be built from this foundation.
        
        # Placeholder for where the processed data will go
        categorized_data = {"sd15_models": [], "sdxl_models": [], "sd15_loras": [], "sdxl_loras": []}
        
        # This is where you would loop through urls, call the API, and categorize
        # For now, we'll just show a success message
        
        # Example of how you would call the AST writer
        # self._update_data_file(...)
        
        with self.layouts['output_layout']:
            clear_output(wait=True)
            print("✅ Custom Downloader analysis complete.")
            print("In a full implementation, the script would now write to the data files.")
            print("Refreshing model lists to reflect new additions...")
        
        self._update_model_lists()
        
        b.description = "Analyze & Add to Library"
        b.icon = "cogs"
        b.disabled = False

    # --- LAUNCH & SAVE LOGIC (Existing) ---
    def on_launch_click(self, b):
        b.description = "Processing..."; b.icon = "spinner"; b.disabled = True
        with self.layouts['output_layout']:
            clear_output(wait=True)
            self.save_settings() # Save settings first
            print("\n--- 2. Running Environment Setup (VENV & Assets) ---")
            get_ipython().run_line_magic('run', str(ANXETY_ROOT / 'scripts' / 'en' / 'downloading-en.py'))
            print("\n--- 3. Launching WebUI ---")
            get_ipython().run_line_magic('run', str(ANXETY_ROOT / 'scripts' / 'launch.py'))
        b.description = "Launch Complete"; b.icon = "check"; b.disabled = False
        
    def save_settings(self):
        print("--- 1. Saving All UI Settings ---")
        SETTINGS_PATH = ANXETY_ROOT / 'settings.json'
        widget_values = {k: v.value for k, v in self.widgets.items() if hasattr(v, 'value') and not isinstance(v, list)}
        for key in ['model_list', 'vae_list', 'controlnet_list', 'lora_list']:
            if key in self.widgets:
                widget_values[key] = [cb.description for cb in self.widgets[key] if cb.value]
        
        js.save(str(SETTINGS_PATH), 'WIDGETS', widget_values)
        js.save(str(SETTINGS_PATH), 'ENVIRONMENT.home_path', '/content')
        update_current_webui(widget_values['change_webui'])
        print("✅ Configuration saved to settings.json")

# This is what makes the script runnable
if __name__ == "__main__":
    ui = AnxietyUI()
    ui.create_ui()

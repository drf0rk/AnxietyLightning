# /content/ANXETY/scripts/en/widgets_en.py (v17.3 - Synchronous Fix)

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
import re
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
        self.api = CivitAiAPI(js.read(ANXETY_ROOT / 'settings.json', 'WIDGETS.civitai_token'))
        self.url_pool = []
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
        # ... (This method remains unchanged)
        self.widgets['sdxl_toggle'] = self.factory.create_toggle_button(description="SDXL Models", value=False, button_style='info', tooltip='Toggle SDXL Models', icon='rocket')
        self.widgets['detailed_download'] = self.factory.create_checkbox(description="Detailed download")
        webui_options = ['ReForge', 'Forge', 'A1111', 'ComfyUI', 'Classic', 'SD-UX']
        self.widgets['change_webui'] = self.factory.create_dropdown('WebUI:', webui_options, 'ReForge')
        self.widgets['commandline_arguments'] = self.factory.create_text(description="Arguments:")
        self.widgets['model_list'], self.widgets['vae_list'], self.widgets['controlnet_list'], self.widgets['lora_list'] = [], [], [], []
        self.widgets['downloader_url_input'] = self.factory.create_text("URL:", placeholder="Paste a single Civitai or Hugging Face URL here")
        self.buttons['downloader_add_to_pool'] = self.factory.create_button("Add to Pool", icon='plus')
        self.widgets['downloader_url_pool'] = widgets.SelectMultiple(options=[], rows=8, description='URL Pool:', disabled=False)
        self.buttons['downloader_analyze'] = self.factory.create_button("Analyze & Add to Library", icon='cogs', button_style='info')

    def _create_layouts(self):
        # ... (This method remains unchanged)
        downloader_input_box = self.factory.create_hbox([self.widgets['downloader_url_input'], self.buttons['downloader_add_to_pool']], layout={'width': '100%'})
        self.widgets['downloader_url_input'].layout.width = '85%'
        downloader_container = self.factory.create_vbox([
            self.factory.create_header("Custom File Downloader"),
            downloader_input_box,
            self.widgets['downloader_url_pool'],
            self.buttons['downloader_analyze'],
            widgets.HTML("<hr>")
        ], class_names=['container'])
        self.layouts['models_box'] = widgets.VBox(self.widgets['model_list'])
        self.layouts['vaes_box'] = widgets.VBox(self.widgets['vae_list'])
        self.layouts['cnets_box'] = widgets.VBox(self.widgets['controlnet_list'])
        self.layouts['loras_box'] = widgets.VBox(self.widgets['lora_list'])
        accordion = widgets.Accordion(children=[
            self.layouts['models_box'], self.layouts['vaes_box'], self.layouts['cnets_box'], self.layouts['loras_box']
        ])
        titles = ['Checkpoints', 'VAEs', 'ControlNets', 'LoRAs']
        for i, title in enumerate(titles): accordion.set_title(i, title)
        self.buttons['launch'] = self.factory.create_button(description="Install, Download & Launch", class_names=['button', 'button_save'], icon='paper-plane')
        top_bar = widgets.HBox([self.widgets['change_webui'], self.widgets['sdxl_toggle'], self.widgets['detailed_download']])
        self.layouts['output_layout'] = widgets.Output()
        self.layouts['main_container'] = widgets.VBox([
            top_bar, self.widgets['commandline_arguments'], downloader_container,
            accordion, self.buttons['launch'], self.layouts['output_layout']
        ])

    def _assign_callbacks(self):
        # ... (This method remains unchanged)
        self.widgets['sdxl_toggle'].observe(self._on_sdxl_toggled, names='value')
        self.widgets['change_webui'].observe(self._on_webui_changed, names='value')
        self.buttons['launch'].on_click(self.on_launch_click)
        self.buttons['downloader_add_to_pool'].on_click(self._on_add_to_pool_clicked)
        self.buttons['downloader_analyze'].on_click(self._on_downloader_analyze_clicked)
        
    def _on_webui_changed(self, change):
        self._update_args_from_webui()

    def _update_args_from_webui(self):
        selected_ui = self.widgets['change_webui'].value
        self.widgets['commandline_arguments'].value = self.webui_selection_args.get(selected_ui, "")

    def _on_add_to_pool_clicked(self, b):
        url = self.widgets['downloader_url_input'].value.strip()
        if url and url not in self.url_pool:
            self.url_pool.append(url)
            self.widgets['downloader_url_pool'].options = self.url_pool
            self.widgets['downloader_url_input'].value = ""

    # --- START OF SYNCHRONOUS FIX ---
    def _on_downloader_analyze_clicked(self, b):
        if not self.url_pool:
            with self.layouts['output_layout']:
                clear_output(wait=True); print("⚠️ URL Pool is empty. Please add at least one URL.")
            return

        b.description = "Processing..."; b.icon = "spinner"; b.disabled = True
        
        # Call the synchronous processing function directly
        self._process_urls_synchronously(self.url_pool)
        
        # Reset UI elements after processing is finished
        self.url_pool = []
        self.widgets['downloader_url_pool'].options = self.url_pool
        b.description = "Analyze & Add to Library"; b.icon = "cogs"; b.disabled = False
        with self.layouts['output_layout']:
            clear_output(wait=True)
            print("✅ Analysis and file writing complete! Refreshing model lists...")
        self._update_model_lists()

    def _process_urls_synchronously(self, urls):
        """Synchronously process a list of URLs and write them to data files."""
        with self.layouts['output_layout']:
            clear_output(wait=True)
            print("Analyzing URLs...")
            for url in urls:
                try:
                    print(f"Processing: {url[:80]}...")
                    if "civitai.com" in url:
                        data = self.api.get_data(url)
                        if data: self._categorize_and_write(data)
                    elif "huggingface.co" in url:
                        self._categorize_and_write(self._get_huggingface_guesses(url))
                    time.sleep(0.5) # Be kind to APIs
                except Exception as e:
                    print(f"❌ Failed to process URL {url}: {e}")
    # --- END OF SYNCHRONOUS FIX ---

    def _get_huggingface_guesses(self, url):
        # ... (This function remains unchanged)
        filename = url.split('/')[-1].split('?')[0]
        file_type = "Checkpoint"
        if "lora" in filename.lower(): file_type = "LORA"
        base_model = "Unknown"
        if "sdxl" in filename.lower() or "xl" in url.lower(): base_model = "SDXL 1.0"
        elif "1.5" in filename.lower() or "1-5" in url.lower(): base_model = "SD 1.5"
        return {'model': {'type': file_type, 'name': filename.rsplit('.', 1)[0]},
                'name': 'v1.0', 'baseModel': base_model,
                'files': [{'name': filename, 'downloadUrl': url.replace("/blob/", "/resolve/")}]}

    def _categorize_and_write(self, data):
        # ... (This function remains unchanged)
        asset_type = data.get('model', {}).get('type', 'Unknown')
        base_model = data.get('baseModel', 'Unknown')
        target_file, target_dict = None, None
        if asset_type == 'LORA':
            target_file = ANXETY_ROOT / 'scripts' / '_

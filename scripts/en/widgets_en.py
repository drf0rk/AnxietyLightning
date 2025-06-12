# /content/ANXETY/scripts/en/widgets_en.py (v17 - Downloader First UI)

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
import asyncio
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
        self.url_pool = [] # List to hold URLs added by the user
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
        # Main UI Widgets
        self.widgets['sdxl_toggle'] = self.factory.create_toggle_button(description="SDXL Models", value=False, button_style='info', tooltip='Toggle SDXL Models', icon='rocket')
        self.widgets['detailed_download'] = self.factory.create_checkbox(description="Detailed download")
        webui_options = ['ReForge', 'Forge', 'A1111', 'ComfyUI', 'Classic', 'SD-UX']
        self.widgets['change_webui'] = self.factory.create_dropdown('WebUI:', webui_options, 'ReForge')
        self.widgets['commandline_arguments'] = self.factory.create_text(description="Arguments:")
        
        # Model Selection Widgets
        self.widgets['model_list'], self.widgets['vae_list'], self.widgets['controlnet_list'], self.widgets['lora_list'] = [], [], [], []
        
        # --- RE-IMPLEMENTED: Custom Downloader Widgets with "Add to Pool" feature ---
        self.widgets['downloader_url_input'] = self.factory.create_text("URL:", placeholder="Paste a single Civitai or Hugging Face URL here")
        self.buttons['downloader_add_to_pool'] = self.factory.create_button("Add to Pool", icon='plus')
        self.widgets['downloader_url_pool'] = widgets.SelectMultiple(options=[], rows=8, description='URL Pool:', disabled=False)
        self.buttons['downloader_analyze'] = self.factory.create_button("Analyze & Add to Library", icon='cogs', button_style='info')

    def _create_layouts(self):
        # --- NEW: Create a dedicated VBox for the custom downloader ---
        downloader_input_box = self.factory.create_hbox([self.widgets['downloader_url_input'], self.buttons['downloader_add_to_pool']], layout={'width': '100%'})
        self.widgets['downloader_url_input'].layout.width = '85%'
        
        downloader_container = self.factory.create_vbox([
            self.factory.create_header("Custom File Downloader"),
            downloader_input_box,
            self.widgets['downloader_url_pool'],
            self.buttons['downloader_analyze'],
            widgets.HTML("<hr>") # Separator
        ], class_names=['container']) # Use the standard container style
        
        # --- Accordion for standard models ---
        self.layouts['models_box'] = widgets.VBox(self.widgets['model_list'])
        self.layouts['vaes_box'] = widgets.VBox(self.widgets['vae_list'])
        self.layouts['cnets_box'] = widgets.VBox(self.widgets['controlnet_list'])
        self.layouts['loras_box'] = widgets.VBox(self.widgets['lora_list'])
        
        accordion = widgets.Accordion(children=[
            self.layouts['models_box'], self.layouts['vaes_box'], self.layouts['cnets_box'], self.layouts['loras_box']
        ])
        titles = ['Checkpoints', 'VAEs', 'ControlNets', 'LoRAs']
        for i, title in enumerate(titles): accordion.set_title(i, title)
        
        # --- REORDERED: Main application layout ---
        self.buttons['launch'] = self.factory.create_button(description="Install, Download & Launch", class_names=['button', 'button_save'], icon='paper-plane')
        top_bar = widgets.HBox([self.widgets['change_webui'], self.widgets['sdxl_toggle'], self.widgets['detailed_download']])
        self.layouts['output_layout'] = widgets.Output()
        
        # The downloader container now appears first in the main layout
        self.layouts['main_container'] = widgets.VBox([
            top_bar,
            self.widgets['commandline_arguments'],
            downloader_container, # <-- MOVED HERE
            accordion,
            self.buttons['launch'],
            self.layouts['output_layout']
        ])

    def _assign_callbacks(self):
        self.widgets['sdxl_toggle'].observe(self._on_sdxl_toggled, names='value')
        self.widgets['change_webui'].observe(self._on_webui_changed, names='value')
        self.buttons['launch'].on_click(self.on_launch_click)
        # --- NEW: Assign callbacks for the new downloader buttons ---
        self.buttons['downloader_add_to_pool'].on_click(self._on_add_to_pool_clicked)
        self.buttons['downloader_analyze'].on_click(self._on_downloader_analyze_clicked)

    # --- NEW: Callback for the "Add to Pool" button ---
    def _on_add_to_pool_clicked(self, b):
        url = self.widgets['downloader_url_input'].value.strip()
        if url and url not in self.url_pool:
            self.url_pool.append(url)
            self.widgets['downloader_url_pool'].options = self.url_pool
            self.widgets['downloader_url_input'].value = "" # Clear input

    def _on_downloader_analyze_clicked(self, b):
        if not self.url_pool:
            with self.layouts['output_layout']:
                clear_output(wait=True); print("⚠️ URL Pool is empty. Please add at least one URL.")
            return

        b.description = "Processing..."; b.icon = "spinner"; b.disabled = True
        with self.layouts['output_layout']:
            clear_output(wait=True); print("Analyzing URLs...")

        asyncio.run(self._process_urls(self.url_pool))
        
        self.url_pool = [] # Clear the pool after processing
        self.widgets['downloader_url_pool'].options = self.url_pool

        b.description = "Analyze & Add to Library"; b.icon = "cogs"; b.disabled = False
        with self.layouts['output_layout']:
            clear_output(wait=True); print("✅ Analysis and file writing complete! Refreshing model lists...")
        self._update_model_lists()

    # --- Backend logic remains the same ---
    async def _process_urls(self, urls):
        # ... (This function remains unchanged)
        for url in urls:
            try:
                if "civitai.com" in url:
                    data = self.api.get_data(url)
                    if data:
                        self._categorize_and_write(data)
                elif "huggingface.co" in url:
                    self._categorize_and_write(self._get_huggingface_guesses(url))
                await asyncio.sleep(0.5) 
            except Exception as e:
                with self.layouts['output_layout']:
                    print(f"❌ Failed to process URL {url}: {e}")

    def _get_huggingface_guesses(self, url):
        # ... (This function remains unchanged)
        filename = url.split('/')[-1].split('?')[0]
        file_type = "Checkpoint"
        if "lora" in filename.lower(): file_type = "LORA"
        base_model = "Unknown"
        if "sdxl" in filename.lower() or "xl" in url.lower(): base_model = "SDXL 1.0"
        elif "1.5" in filename.lower() or "1-5" in url.lower(): base_model = "SD 1.5"
        return {
            'model': {'type': file_type, 'name': filename.rsplit('.', 1)[0]},
            'name': 'v1.0', 'baseModel': base_model,
            'files': [{'name': filename, 'downloadUrl': url.replace("/blob/", "/resolve/")}]
        }

    def _categorize_and_write(self, data):
        # ... (This function remains unchanged)
        asset_type = data.get('model', {}).get('type', 'Unknown')
        base_model = data.get('baseModel', 'Unknown')
        target_file, target_dict = None, None
        if asset_type == 'LORA':
            target_file = ANXETY_ROOT / 'scripts' / '_loras-data.py'
            target_dict = 'sdxl_loras' if 'SDXL' in base_model or 'Pony' in base_model else 'sd15_loras'
        elif asset_type == 'Checkpoint':
            if 'SDXL' in base_model or 'Pony' in base_model:
                target_file = ANXETY_ROOT / 'scripts' / '_xl-models-data.py'
                target_dict = 'sdxl_models_data'
            else:
                target_file = ANXETY_ROOT / 'scripts' / '_models-data.py'
                target_dict = 'sd15_model_data'
        if not target_file or not target_dict:
            with self.layouts['output_layout']: print(f"⚠️ Could not categorize model '{data.get('model', {}).get('name')}'. Skipping.")
            return
        display_name = f"{data.get('model', {}).get('name', 'Unknown')} - {data.get('name', 'v1.0')}"
        file_info = data.get('files', [{}])[0]
        download_url = file_info.get('downloadUrl', '').split('?')[0]
        file_name = file_info.get('name', 'unknown.safetensors')
        new_entry = {'display_name': display_name, 'url': download_url, 'filename': file_name}
        self._update_data_file_with_ast(target_file, target_dict, new_entry)
        
    def _update_data_file_with_ast(self, file_path, dict_name, new_entry):
        # ... (This function remains unchanged)
        if not file_path.exists():
            with self.layouts['output_layout']: print(f"❌ Error: Data file not found at {file_path}"); return
        with open(file_path, 'r', encoding='utf-8') as f: source_code = f.read()
        tree = ast.parse(source_code)
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == dict_name:
                        dict_node = node.value
                        if isinstance(dict_node, ast.Dict):
                            if any(isinstance(k, ast.Constant) and k.value == new_entry['display_name'] for k in dict_node.keys):
                                with self.layouts['output_layout']: print(f"ℹ️ Model '{new_entry['display_name']}' already exists. Skipping."); return
                            key_node = ast.Constant(value=new_entry['display_name'])
                            value_node = ast.Dict(keys=[ast.Constant(value='url'), ast.Constant(value='name')], values=[ast.Constant(value=new_entry['url']), ast.Constant(value=new_entry['filename'])])
                            dict_node.keys.append(key_node)
                            dict_node.values.append(value_node)
                            break
        else:
            with self.layouts['output_layout']: print(f"❌ Error: Could not find dictionary '{dict_name}' in {file_path}"); return
        new_source_code = ast.unparse(tree)
        with open(file_path, 'w', encoding='utf-8') as f: f.write(new_source_code)
        with self.layouts['output_layout']: print(f"✅ Successfully added '{new_entry['display_name']}' to {dict_name}.")
        
    def _on_sdxl_toggled(self, change): self._update_model_lists()
    def _update_model_lists(self):
        # ... (This function remains unchanged)
        is_xl = self.widgets['sdxl_toggle'].value
        models_py_path = ANXETY_ROOT / 'scripts' / ('_xl-models-data.py' if is_xl else '_models-data.py')
        loras_py_path = ANXETY_ROOT / 'scripts' / '_loras-data.py'
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
        
    def on_launch_click(self, b):
        # ... (This function remains unchanged)
        b.description = "Processing..."; b.icon = "spinner"; b.disabled = True
        with self.layouts['output_layout']:
            clear_output(wait=True)
            self.save_settings()
            print("\n--- 2. Running Environment Setup (VENV & Assets) ---")
            get_ipython().run_line_magic('run', str(ANXETY_ROOT / 'scripts' / 'en' / 'downloading-en.py'))
            print("\n--- 3. Launching WebUI ---")
            get_ipython().run_line_magic('run', str(ANXETY_ROOT / 'scripts' / 'launch.py'))
        b.description = "Launch Complete"; b.icon = "check"; b.disabled = False
        
    def save_settings(self):
        # ... (This function remains unchanged)
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

if __name__ == "__main__":
    ui = AnxietyUI()
    ui.create_ui()

# /content/ANXETY/scripts/en/widgets_en.py (v19.1 - API Method Fix)

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
        self.processed_data = []
        self.review_widgets = {}
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
        self.widgets['model_list'], self.widgets['vae_list'], self.widgets['controlnet_list'], self.widgets['lora_list'] = [], [], [], []
        self.widgets['downloader_url_input'] = self.factory.create_text("URL:", placeholder="Paste a single Civitai or Hugging Face URL here")
        self.buttons['downloader_add_to_pool'] = self.factory.create_button("Add to Pool", icon='plus')
        self.widgets['downloader_url_pool'] = widgets.SelectMultiple(options=[], rows=8, description='URL Pool:', disabled=False)
        self.buttons['downloader_review'] = self.factory.create_button("Next: Review & Categorize", icon='arrow-right', button_style='info')

    def _create_layouts(self):
        self.layouts['main_output_area'] = widgets.VBox()
        downloader_input_box = self.factory.create_hbox([self.widgets['downloader_url_input'], self.buttons['downloader_add_to_pool']], layout={'width': '100%'})
        self.widgets['downloader_url_input'].layout.width = '85%'
        downloader_container = self.factory.create_vbox([
            self.factory.create_header("Custom File Downloader"),
            downloader_input_box,
            self.widgets['downloader_url_pool'],
            self.buttons['downloader_review'],
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
        self.layouts['initial_view'] = widgets.VBox([
            top_bar, self.widgets['commandline_arguments'], downloader_container,
            accordion, self.buttons['launch']
        ])
        self.layouts['main_output_area'].children = [self.layouts['initial_view']]
        self.layouts['main_container'] = self.layouts['main_output_area']

    def _assign_callbacks(self):
        self.widgets['sdxl_toggle'].observe(self._on_sdxl_toggled, names='value')
        self.widgets['change_webui'].observe(self._on_webui_changed, names='value')
        self.buttons['launch'].on_click(self.on_launch_click)
        self.buttons['downloader_add_to_pool'].on_click(self._on_add_to_pool_clicked)
        self.buttons['downloader_review'].on_click(self._on_downloader_review_clicked)

    def _on_webui_changed(self, change): self._update_args_from_webui()
    def _update_args_from_webui(self):
        selected_ui = self.widgets['change_webui'].value
        self.widgets['commandline_arguments'].value = self.webui_selection_args.get(selected_ui, "")

    def _on_add_to_pool_clicked(self, b):
        url = self.widgets['downloader_url_input'].value.strip()
        if url and url not in self.url_pool:
            self.url_pool.append(url)
            self.widgets['downloader_url_pool'].options = self.url_pool
            self.widgets['downloader_url_input'].value = ""

    def _on_downloader_review_clicked(self, b):
        if not self.url_pool: print("⚠️ URL Pool is empty."); return
        b.description = "Processing..."; b.icon = "spinner"; b.disabled = True
        self._build_and_display_review_stage()
        b.description = "Next: Review & Categorize"; b.icon = "arrow-right"; b.disabled = False

    def _build_and_display_review_stage(self):
        self.processed_data = []
        for url in self.url_pool:
            # --- START OF FIX ---
            if "civitai.com" in url:
                data = self.api.get_data(url)
                if data:
                    self.processed_data.append(self._structure_civitai_data(data))
            else: # Hugging Face
                data = self._get_huggingface_guesses(url)
                if data: self.processed_data.append(data)
            # --- END OF FIX ---
        
        type_order = {'Checkpoint': 0, 'LORA': 1, 'VAE': 2}
        self.processed_data.sort(key=lambda x: (type_order.get(x.get('type', 99), 99), x.get('name', '')))

        css = """<style> .review-row { border-radius: 5px; padding: 10px; margin-bottom: 5px; border-left: 5px solid; } .review-row-model { border-left-color: #7289DA; background-color: rgba(114, 137, 218, 0.1); } .review-row-lora { border-left-color: #43B581; background-color: rgba(67, 181, 129, 0.1); } .review-row-hf { border-left-color: #FAA61A; background-color: rgba(250, 166, 26, 0.1); } </style>"""
        display(HTML(css))

        review_rows = []
        self.review_widgets = {}
        
        for i, item in enumerate(self.processed_data):
            is_hf = item.get('source') == 'HuggingFace'
            name_label = self.factory.create_html(f"<b>{item.get('name', 'Unknown')}</b> ({item.get('source', 'Unknown')})")
            
            # This logic needs to correctly handle the structure of Civitai vs HF data
            type_val = item.get('type')
            base_model_val = item.get('baseModel', 'Unknown') if is_hf else item.get('baseModel')

            type_dropdown = self.factory.create_dropdown(options=['Checkpoint', 'LORA', 'VAE'], value=type_val, description="Asset Type:", disabled=not is_hf)
            base_model_dropdown = self.factory.create_dropdown(options=['SD 1.5', 'SDXL 1.0', 'Pony', 'Unknown'], value=base_model_val, description="Base Model:", disabled=not is_hf)
            
            file_options = {f['name']: f['downloadUrl'] for f in item.get('files', [])}
            file_dropdown = self.factory.create_dropdown(options=list(file_options.keys()), description="File:")

            self.review_widgets[i] = {"name": item.get('name'), "type": type_dropdown, "base_model": base_model_dropdown, "file_url_map": file_options, "file_selection": file_dropdown}
            
            row = widgets.VBox([name_label, type_dropdown, base_model_dropdown, file_dropdown], layout={'padding': '10px'})
            css_class = 'review-row'
            if is_hf: css_class += ' review-row-hf'
            elif type_val == 'Checkpoint': css_class += ' review-row-model'
            elif type_val == 'LORA': css_class += ' review-row-lora'
            row.add_class(css_class)
            
            review_rows.append(row)
        
        confirm_button = self.factory.create_button("Confirm & Add to Library", icon='check', class_names=['button_save'])
        confirm_button.on_click(self._on_confirm_and_write_clicked)
        
        review_stage_layout = widgets.VBox([self.factory.create_header("Downloader - Stage 2: Review & Confirm"), *review_rows, confirm_button])
        self.layouts['main_output_area'].children = [review_stage_layout]
        
    def _on_confirm_and_write_clicked(self, b):
        b.description = "Writing..."; b.icon = "spinner"; b.disabled = True
        output_log = widgets.Output()
        display(output_log)
        with output_log:
            print("--- Writing Selections to Data Scripts ---")
            for i, item_widgets in self.review_widgets.items():
                selected_file_name = item_widgets['file_selection'].value
                
                # Reconstruct data with user's choices
                final_data = {
                    'model': {'type': item_widgets['type'].value, 'name': item_widgets['name']},
                    'name': 'v1.0',
                    'baseModel': item_widgets['base_model'].value,
                    'files': [{'name': selected_file_name, 'downloadUrl': item_widgets['file_url_map'][selected_file_name]}]
                }
                self._categorize_and_write(final_data)
        
        print("✅ All items processed. Returning to the main menu...")
        time.sleep(2)
        self.url_pool = []
        self.widgets['downloader_url_pool'].options = []
        self._update_model_lists()
        self.layouts['main_output_area'].children = [self.layouts['initial_view']]

    def _get_huggingface_guesses(self, url):
        filename = url.split('/')[-1].split('?')[0]
        file_type = "Checkpoint"
        if "lora" in filename.lower(): file_type = "LORA"
        base_model = "Unknown"
        if "sdxl" in filename.lower() or "xl" in url.lower(): base_model = "SDXL 1.0"
        elif "1.5" in filename.lower() or "1-5" in url.lower(): base_model = "SD 1.5"
        return {'source': 'HuggingFace', 'name': filename.rsplit('.', 1)[0], 'type': file_type, 'baseModel': base_model, 'files': [{'name': filename, 'downloadUrl': url.replace("/blob/", "/resolve/")}]}

    def _structure_civitai_data(self, data):
        """Structures the raw dict from get_data"""
        return {'source': 'Civitai', 'name': data.get('model', {}).get('name'), 'type': data.get('model', {}).get('type'),
                'baseModel': data.get('baseModel'), 'files': data.get('files', [])}

    def _categorize_and_write(self, data):
        asset_type = data.get('model', {}).get('type', 'Unknown')
        base_model = data.get('baseModel', 'Unknown')
        target_file, target_dict = None, None
        is_sdxl_type = 'SDXL' in base_model or 'Pony' in base_model
        if asset_type == 'LORA':
            target_file = ANXETY_ROOT / 'scripts' / '_loras-data.py'
            target_dict = 'sdxl_loras' if is_sdxl_type else 'sd15_loras'
        elif asset_type == 'Checkpoint':
            target_file = ANXETY_ROOT / 'scripts' / ('_xl-models-data.py' if is_sdxl_type else '_models-data.py')
            target_dict = 'sdxl_models_data' if is_sdxl_type else 'sd15_model_data'
        if not target_file or not target_dict: print(f"⚠️ Could not categorize model '{data.get('model', {}).get('name')}'. Skipping.") ; return
        display_name = f"{data.get('model', {}).get('name', 'Unknown')} - {data.get('name', 'v1.0')}"
        file_info = data.get('files', [{}])[0]
        download_url = file_info.get('downloadUrl', '').split('?')[0]
        file_name = file_info.get('name', 'unknown.safetensors')
        new_entry = {'display_name': display_name, 'url': download_url, 'filename': file_name}
        self._update_data_file_with_ast(target_file, target_dict, new_entry)
        
    def _update_data_file_with_ast(self, file_path, dict_name, new_entry):
        if not file_path.exists(): print(f"❌ Error: Data file not found at {file_path}"); return
        with open(file_path, 'r', encoding='utf-8') as f: source_code = f.read()
        tree = ast.parse(source_code)
        found_and_modified = False
        if file_path.name == '_loras-data.py':
            for node in ast.walk(tree):
                if isinstance(node, ast.Assign) and node.targets[0].id == 'lora_data':
                    for i, key in enumerate(node.value.keys):
                        if isinstance(key, ast.Constant) and key.value == dict_name:
                            dict_node = node.value.values[i]
                            if isinstance(dict_node, ast.Dict):
                                if any(isinstance(k, ast.Constant) and k.value == new_entry['display_name'] for k in dict_node.keys):
                                    print(f"ℹ️ LoRA '{new_entry['display_name']}' already exists. Skipping.")
                                    found_and_modified = True; break
                                key_node = ast.Constant(value=new_entry['display_name'])
                                value_node = ast.List(elts=[ast.Dict(keys=[ast.Constant(value='url'), ast.Constant(value='name')], values=[ast.Constant(value=new_entry['url']), ast.Constant(value=new_entry['filename'])])])
                                dict_node.keys.append(key_node)
                                dict_node.values.append(value_node)
                                found_and_modified = True; break
                    if found_and_modified: break
        else:
            for node in ast.walk(tree):
                if isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name) and target.id == dict_name:
                            dict_node = node.value
                            if isinstance(dict_node, ast.Dict):
                                if any(isinstance(k, ast.Constant) and k.value == new_entry['display_name'] for k in dict_node.keys):
                                    print(f"ℹ️ Model '{new_entry['display_name']}' already exists. Skipping."); return
                                key_node = ast.Constant(value=new_entry['display_name'])
                                value_node = ast.Dict(keys=[ast.Constant(value='url'), ast.Constant(value='name')], values=[ast.Constant(value=new_entry['url']), ast.Constant(value=new_entry['filename'])])
                                dict_node.keys.append(key_node)
                                dict_node.values.append(value_node)
                                found_and_modified = True; break
                if found_and_modified: break
        if not found_and_modified: print(f"❌ Error: Could not find or modify dictionary '{dict_name}' in {file_path}"); return
        new_source_code = ast.unparse(tree)
        with open(file_path, 'w', encoding='utf-8') as f: f.write(new_source_code)
        print(f"✅ Successfully added '{new_entry['display_name']}' to {dict_name}.")
            
    def _on_sdxl_toggled(self, change): self._update_model_lists()
    def _update_model_lists(self):
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
        b.description = "Processing..."; b.icon = "spinner"; b.disabled = True
        with self.layouts['main_output_area']:
            clear_output(wait=True)
            self.save_settings()
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

if __name__ == "__main__":
    ui = AnxietyUI()
    ui.create_ui()

# /content/ANXETY/scripts/en/widgets_en.py (v20.2 - URL Pool Textarea & Debugging)

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
        self.url_pool = [] # This will still store the list of individual URLs
        self.processed_data = []
        self.review_widgets = {}
        self.selections = {'model_list': set(), 'vae_list': set(), 'controlnet_list': set(), 'lora_list': set()}
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
        
        # Changed to Textarea for copy-paste functionality
        self.widgets['downloader_url_input'] = self.factory.create_textarea("URLs:", placeholder="Paste multiple Civitai or Hugging Face URLs here (one per line or comma-separated)")
        self.buttons['downloader_add_to_pool'] = self.factory.create_button("Add All to Pool", icon='plus')
        
        # The pool itself will also be a textarea for display and re-copying
        self.widgets['downloader_url_pool'] = self.factory.create_textarea(description='Current URL Pool:', rows=8, disabled=False)
        self.widgets['downloader_url_pool'].layout.width = '100%' # Ensure it uses full width
        
        self.buttons['downloader_review'] = self.factory.create_button("Next: Review & Categorize", icon='arrow-right', button_style='info')

    def _create_layouts(self):
        self.layouts['main_output_area'] = widgets.Output() 
        
        downloader_input_box = self.factory.create_hbox([self.widgets['downloader_url_input'], self.buttons['downloader_add_to_pool']], layout={'width': '100%'})
        self.widgets['downloader_url_input'].layout.width = '85%'
        
        downloader_container = self.factory.create_vbox([
            self.factory.create_header("Custom File Downloader"), 
            downloader_input_box,
            widgets.HTML("<h4>Current URL Pool:</h4>"), # Explicit header for the pool
            self.widgets['downloader_url_pool'], 
            self.buttons['downloader_review'], 
            widgets.HTML("<hr>")
        ], class_names=['container'])
        
        self.layouts['models_box'], self.layouts['vaes_box'], self.layouts['cnets_box'], self.layouts['loras_box'] = widgets.VBox(), widgets.VBox(), widgets.VBox(), widgets.VBox()
        accordion = widgets.Accordion(children=[self.layouts['models_box'], self.layouts['vaes_box'], self.layouts['cnets_box'], self.layouts['loras_box']])
        titles = ['Checkpoints', 'VAEs', 'ControlNets', 'LoRAs']
        for i, title in enumerate(titles): accordion.set_title(i, title)
        
        self.buttons['launch'] = self.factory.create_button(description="Install, Download & Launch", class_names=['button', 'button_save'], icon='paper-plane')
        top_bar = widgets.HBox([self.widgets['change_webui'], self.widgets['sdxl_toggle'], self.widgets['detailed_download']])
        self.layouts['initial_view'] = widgets.VBox([top_bar, self.widgets['commandline_arguments'], downloader_container, accordion, self.buttons['launch']])
        
        self.layouts['main_container'] = widgets.VBox([self.layouts['initial_view'], self.layouts['main_output_area']])

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
        with self.layouts['main_output_area']:
            clear_output(wait=True)
            new_urls_raw = self.widgets['downloader_url_input'].value.strip()
            if not new_urls_raw:
                print("ℹ️ No URLs provided to add.")
                return
            
            # Split by lines and then by commas, filtering out empty strings
            new_urls = [url.strip() for line in new_urls_raw.splitlines() for url in line.split(',') if url.strip()]
            
            added_count = 0
            for url in new_urls:
                if url and url not in self.url_pool:
                    self.url_pool.append(url)
                    added_count += 1
            
            self.widgets['downloader_url_input'].value = "" # Clear input after adding
            self.widgets['downloader_url_pool'].value = "\n".join(self.url_pool) # Update textarea display
            print(f"✅ Added {added_count} new URLs to the pool. Total URLs: {len(self.url_pool)}")


    def _on_downloader_review_clicked(self, b):
        with self.layouts['main_output_area']:
            clear_output(wait=True)
            print("Starting URL review and categorization process...")
            if not self.url_pool:
                print("⚠️ URL Pool is empty. Please add URLs first.")
                b.description = "Next: Review & Categorize"; b.icon = "arrow-right"; b.disabled = False
                return
            
            b.description = "Processing..."; b.icon = "spinner"; b.disabled = True
            print(f"Processing {len(self.url_pool)} URLs from the pool.")
            self._build_and_display_review_stage()
            b.description = "Next: Review & Categorize"; b.icon = "arrow-right"; b.disabled = False
            print("URL review process initiated. Please check the review panel.")
        
    def _build_and_display_review_stage(self):
        self.processed_data = []
        with self.layouts['main_output_area']: # Direct output here
            print("Fetching data for URLs. This might take a moment...")
            for url in self.url_pool:
                print(f"  Processing URL: {url}")
                data = None
                try:
                    if "civitai.com" in url:
                        print(f"    Detected Civitai URL. Calling CivitAiAPI.get_model...")
                        data = self.api.get_model(url)
                        if data:
                            print(f"    Civitai API returned data for: {data.name} (Type: {data.type})")
                        else:
                            print(f"    Civitai API returned no data or failed for {url}.")
                    elif "huggingface.co" in url:
                        print(f"    Detected Hugging Face URL. Guessing asset type...")
                        data = self._get_huggingface_guesses(url)
                        if data:
                            print(f"    Guessed HF data for: {data.get('name')} (Type: {data.get('type')})")
                        else:
                            print(f"    Hugging Face guessing failed for {url}.")
                    else:
                        print(f"    Unsupported URL type: {url}. Skipping.")

                    if data: 
                        self.processed_data.append(data)
                    else:
                        print(f"    ⚠️ Skipping {url} due to no data or unsupported format.")
                except Exception as e:
                    print(f"    ❌ Error processing {url}: {e}", file=sys.stderr)
            
            if not self.processed_data:
                print("❌ No valid model data could be retrieved from the provided URLs. Please check URLs and try again.")
                # Optionally return to initial view or display a message
                self.layouts['main_output_area'].children = [self.layouts['initial_view']]
                return


            print(f"Successfully processed {len(self.processed_data)} URLs. Building review UI.")
            type_order = {'Checkpoint': 0, 'LORA': 1, 'VAE': 2, 'ControlNet': 3, 'Embeddings': 4} # Added more types for sorting
            self.processed_data.sort(key=lambda x: (type_order.get(x.type if hasattr(x, 'type') else x.get('type', 'Unknown'), 99), x.name if hasattr(x, 'name') else x.get('name', '')))

            css = """<style> .review-row { border-radius: 5px; padding: 10px; margin-bottom: 5px; border-left: 5px solid; } .review-row-model { border-left-color: #7289DA; background-color: rgba(114, 137, 218, 0.1); } .review-row-lora { border-left-color: #43B581; background-color: rgba(67, 181, 129, 0.1); } .review-row-hf { border-left-color: #FAA61A; background-color: rgba(250, 166, 26, 0.1); } </style>"""
            display(HTML(css))

            review_rows = []
            self.review_widgets = {}
            for i, item in enumerate(self.processed_data):
                is_hf = isinstance(item, dict)
                name = item.get('name') if is_hf else item.name
                source = item.get('source', 'Civitai') if is_hf else 'Civitai'
                
                name_label = self.factory.create_html(f"<b>{name}</b> ({source})")
                
                # Ensure type_val matches expected options, default to 'Checkpoint' if 'Unknown'
                type_options = ['Checkpoint', 'LORA', 'VAE', 'ControlNet', 'Embedding', 'TextualInversion', 'Hypernetwork', 'Other'] # Expanded options
                type_val = item.get('type') if is_hf else item.type
                if type_val not in type_options:
                    type_val = 'Other' # Default to 'Other' for unknown types
                type_dropdown = self.factory.create_dropdown(options=type_options, value=type_val, description="Asset Type:", disabled=not is_hf)
                
                base_model_options = ['SD 1.5', 'SDXL 1.0', 'Pony', 'Unknown', 'Other'] # Expanded options
                base_model_val = item.get('baseModel') if is_hf else (item.model_versions[0].base_model if item.model_versions else 'Unknown')
                if base_model_val not in base_model_options:
                    base_model_val = 'Other'
                base_model_dropdown = self.factory.create_dropdown(options=base_model_options, value=base_model_val, description="Base Model:", disabled=not is_hf)

                row_widgets = [name_label, type_dropdown, base_model_dropdown]
                
                file_dropdown = None
                if not is_hf and hasattr(item, 'model_versions') and item.model_versions:
                    versions_map = {v.name: v for v in item.model_versions}
                    version_dropdown = self.factory.create_dropdown(options=list(versions_map.keys()), description="Model Version:")
                    
                    def _update_file_options(change, item_index=i):
                        selected_version_obj = versions_map[change['new']]
                        file_opts = {f.name: f.download_url for f in selected_version_obj.files}
                        self.review_widgets[item_index]['file_selection'].options = list(file_opts.keys())
                        self.review_widgets[item_index]['file_url_map'] = file_opts
                        # Update default selected file to the first in the new list if available
                        if file_opts:
                            self.review_widgets[item_index]['file_selection'].value = list(file_opts.keys())[0]

                    version_dropdown.observe(_update_file_options, names='value')
                    
                    initial_files = {f.name: f.download_url for f in item.model_versions[0].files}
                    file_dropdown = self.factory.create_dropdown(options=list(initial_files.keys()), description="File:")
                    # Set initial value if available
                    if initial_files:
                        file_dropdown.value = list(initial_files.keys())[0]
                    row_widgets.append(version_dropdown)
                elif is_hf: # For Hugging Face, there's usually just one "file" guess
                    initial_files = {f['name']: f['downloadUrl'] for f in item.get('files', [])}
                    file_dropdown = self.factory.create_dropdown(options=list(initial_files.keys()), description="File:", disabled=True)
                    if initial_files:
                        file_dropdown.value = list(initial_files.keys())[0]
                
                if file_dropdown: # Only append if a file dropdown was created
                    row_widgets.append(file_dropdown)
                else: # Fallback if no file_dropdown could be created (e.g. no versions/files)
                    print(f"    ⚠️ No downloadable files found for {name}. Skipping file selection for this item.")
                    continue # Skip this item if no downloadable files are found.

                self.review_widgets[i] = {"name": name, "type": type_dropdown, "base_model": base_model_dropdown, "file_url_map": initial_files, "file_selection": file_dropdown}
                
                row_layout = widgets.Layout(padding='10px', margin='5px 0 0 0', border_radius='5px')
                if is_hf: row_layout.border = '3px solid #FAA61A'; row_layout.background = 'rgba(250, 166, 26, 0.1)'
                elif type_val == 'Checkpoint': row_layout.border = '3px solid #7289DA'; row_layout.background = 'rgba(114, 137, 218, 0.1)'
                elif type_val == 'LORA': row_layout.border = '3px solid #43B581'; row_layout.background = 'rgba(67, 181, 129, 0.1)'
                elif type_val == 'VAE': row_layout.border = '3px solid #b26eeb'; row_layout.background = 'rgba(178, 110, 235, 0.1)' # Example color for VAE
                elif type_val == 'ControlNet': row_layout.border = '3px solid #6ee7b7'; row_layout.background = 'rgba(110, 231, 183, 0.1)' # Example color for ControlNet
                
                row = widgets.VBox(row_widgets, layout=row_layout)
                review_rows.append(row)
            
            if not review_rows:
                print("❌ No items were successfully prepared for the review stage. Returning to main menu.")
                self.layouts['main_output_area'].children = [self.layouts['initial_view']]
                return

            confirm_button = self.factory.create_button("Confirm & Add to Library", icon='check', class_names=['button_save'])
            confirm_button.on_click(self._on_confirm_and_write_clicked)
            review_stage_layout = widgets.VBox([self.factory.create_header("Downloader - Stage 2: Review & Confirm"), *review_rows, confirm_button])
            self.layouts['main_output_area'].children = [review_stage_layout]
            print("Review panel displayed. Please categorize and confirm your selections.")


    def _on_confirm_and_write_clicked(self, b):
        b.description = "Writing..."; b.icon = "spinner"; b.disabled = True
        with self.layouts['main_output_area']:
            clear_output(wait=True)
            print("--- Writing Selections to Data Scripts ---")
            success_count = 0
            for i, item_widgets in self.review_widgets.items():
                try:
                    selected_file_name = item_widgets['file_selection'].value
                    # Re-verify that selected_file_name is valid
                    if not selected_file_name or selected_file_name not in item_widgets['file_url_map']:
                        print(f"⚠️ Skipping '{item_widgets['name']}': No valid file selected or found in map. This might indicate an issue with initial data fetching.", file=sys.stderr)
                        continue

                    final_data = {'model': {'type': item_widgets['type'].value, 'name': item_widgets['name']}, 
                                  'name': selected_file_name.rsplit('.',1)[0], # Use filename as version name
                                  'baseModel': item_widgets['base_model'].value,
                                  'files': [{'name': selected_file_name, 'downloadUrl': item_widgets['file_url_map'][selected_file_name]}]}
                    self._categorize_and_write(final_data)
                    success_count += 1
                except Exception as e:
                    print(f"❌ Error processing item '{item_widgets.get('name', 'Unknown')}': {e}", file=sys.stderr)

            print(f"✅ Processed {success_count} items. Returning to main menu...")
            time.sleep(2)
            self.url_pool = []; self.widgets['downloader_url_pool'].value = "" # Clear pool and textarea
            self._update_model_lists()
            self.layouts['main_output_area'].children = [self.layouts['initial_view']]
        b.description = "Confirm & Add to Library"; b.icon = "check"; b.disabled = False # Reset button state


    def _get_huggingface_guesses(self, url):
        with self.layouts['main_output_area']:
            print(f"  Attempting to guess Hugging Face asset details for: {url}")
            try:
                filename = url.split('/')[-1].split('?')[0]
                file_type = "Checkpoint"; base_model = "Unknown"
                
                # More robust guessing
                if any(ext in filename.lower() for ext in ['.safetensors', '.ckpt', '.pt', '.bin']):
                    if "lora" in filename.lower(): file_type = "LORA"
                    elif "vae" in filename.lower(): file_type = "VAE"
                    elif "control" in filename.lower(): file_type = "ControlNet"
                    elif "embed" in filename.lower() or "textualinversion" in filename.lower(): file_type = "Embedding"
                    elif "hypernetwork" in filename.lower(): file_type = "Hypernetwork"
                    else: file_type = "Checkpoint" # Default for .safetensors, .ckpt etc.
                
                if "sdxl" in filename.lower() or "xl" in url.lower(): base_model = "SDXL 1.0"
                elif "pony" in filename.lower(): base_model = "Pony"
                elif "1.5" in filename.lower() or "1-5" in url.lower(): base_model = "SD 1.5"
                else: base_model = "Unknown" # Default for others

                guessed_name = filename.rsplit('.', 1)[0]
                download_url_clean = url.replace("/blob/", "/resolve/").split('?')[0] # Clean URL for download

                print(f"    Guessed Type: {file_type}, Base Model: {base_model}, Name: {guessed_name}")
                return {'source': 'HuggingFace', 'name': guessed_name, 'type': file_type, 'baseModel': base_model, 'files': [{'name': filename, 'downloadUrl': download_url_clean}]}
            except Exception as e:
                print(f"    ❌ Error guessing HF details for {url}: {e}", file=sys.stderr)
                return None


    def _categorize_and_write(self, data):
        with self.layouts['main_output_area']:
            asset_type = data.get('model', {}).get('type', 'Unknown')
            base_model = data.get('baseModel', 'Unknown')
            target_file, target_dict = None, None
            is_sdxl_type = 'SDXL' in base_model or 'Pony' in base_model # Pony models also go to XL data files

            print(f"  Categorizing: '{data.get('model', {}).get('name')}' (Type: {asset_type}, Base: {base_model})")

            if asset_type == 'LORA':
                target_file = ANXETY_ROOT / 'scripts' / '_loras-data.py'
                target_dict = 'sdxl_loras' if is_sdxl_type else 'sd15_loras'
            elif asset_type == 'Checkpoint':
                target_file = ANXETY_ROOT / 'scripts' / ('_xl-models-data.py' if is_sdxl_type else '_models-data.py')
                target_dict = 'sdxl_models_data' if is_sdxl_type else 'sd15_model_data'
            elif asset_type == 'VAE':
                target_file = ANXETY_ROOT / 'scripts' / ('_xl-models-data.py' if is_sdxl_type else '_models-data.py')
                target_dict = 'sdxl_vae_data' if is_sdxl_type else 'sd15_vae_data'
            elif asset_type == 'ControlNet':
                target_file = ANXETY_ROOT / 'scripts' / ('_xl-models-data.py' if is_sdxl_type else '_models-data.py') # ControlNets often live in XL data files too
                target_dict = 'controlnet_list' # ControlNet list is usually combined for SD1.5/XL
            elif asset_type in ['Embedding', 'TextualInversion']: # Embeddings/TextualInversions
                target_file = ANXETY_ROOT / 'scripts' / '_embeddings-data.py' # Assuming a new data file for embeddings
                target_dict = 'sdxl_embeddings' if is_sdxl_type else 'sd15_embeddings'
            elif asset_type == 'Hypernetwork':
                target_file = ANXETY_ROOT / 'scripts' / '_hypernetworks-data.py' # Assuming a new data file
                target_dict = 'sdxl_hypernetworks' if is_sdxl_type else 'sd15_hypernetworks'

            if not target_file or not target_dict: 
                print(f"    ⚠️ Could not categorize model '{data.get('model', {}).get('name', 'Unknown')}' into known asset types/base models. Skipping writing to data file.", file=sys.stderr); 
                return

            display_name = f"{data.get('model', {}).get('name', 'Unknown')} - {data.get('name', 'v1.0')}"
            file_info = data.get('files', [{}])[0]
            download_url = file_info.get('downloadUrl', '').split('?')[0] # Remove query params
            file_name = file_info.get('name', 'unknown.safetensors') # Default filename

            new_entry = {'display_name': display_name, 'url': download_url, 'filename': file_name}
            print(f"    Attempting to write new entry to {target_file.name}, dictionary '{target_dict}'.")
            self._update_data_file_with_ast(target_file, target_dict, new_entry, asset_type) # Pass asset_type for specific handling
        
    def _update_data_file_with_ast(self, file_path, dict_name, new_entry, asset_type):
        with self.layouts['main_output_area']:
            if not file_path.exists(): 
                print(f"    ❌ Error: Data file not found at {file_path}. Cannot update.", file=sys.stderr); return
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f: 
                    source_code = f.read()
                tree = ast.parse(source_code)
                found_and_modified = False

                for node in ast.walk(tree):
                    if isinstance(node, ast.Assign):
                        for target in node.targets:
                            # Check if the target is a Name node and its ID matches dict_name
                            if isinstance(target, ast.Name) and target.id == dict_name:
                                dict_node = node.value
                                if isinstance(dict_node, ast.Dict):
                                    # Check if the display_name already exists to avoid duplicates
                                    if any(isinstance(k, ast.Constant) and k.value == new_entry['display_name'] for k in dict_node.keys):
                                        print(f"    ℹ️ '{asset_type}' '{new_entry['display_name']}' already exists in {dict_name}. Skipping addition.")
                                        found_and_modified = True
                                        break
                                    
                                    key_node = ast.Constant(value=new_entry['display_name'])
                                    
                                    # Handle different value structures for loras vs. models/vaes
                                    if asset_type == 'LORA' or asset_type == 'ControlNet': # LoRAs and ControlNets are lists of dicts
                                        value_node = ast.List(elts=[ast.Dict(keys=[ast.Constant(value='url'), ast.Constant(value='name')], 
                                                                             values=[ast.Constant(value=new_entry['url']), ast.Constant(value=new_entry['filename'])])])
                                    else: # Models, VAEs, Embeddings, Hypernetworks are single dicts
                                        value_node = ast.Dict(keys=[ast.Constant(value='url'), ast.Constant(value='name')], 
                                                              values=[ast.Constant(value=new_entry['url']), ast.Constant(value=new_entry['filename'])])
                                    
                                    dict_node.keys.append(key_node)
                                    dict_node.values.append(value_node)
                                    found_and_modified = True
                                    print(f"    Successfully added '{new_entry['display_name']}' to '{dict_name}' in '{file_path.name}'.")
                                    break # Break from inner loop over targets
                        if found_and_modified:
                            break # Break from outer loop over nodes if modification happened

                if not found_and_modified: 
                    print(f"    ❌ Error: Could not find dictionary '{dict_name}' or add '{new_entry['display_name']}' in {file_path}. Please check data file format.", file=sys.stderr); return
                
                new_source_code = ast.unparse(tree)
                with open(file_path, 'w', encoding='utf-8') as f: 
                    f.write(new_source_code)
                print(f"    ✅ Successfully updated {file_path.name}.")
            except Exception as e:
                print(f"    ❌ Critical Error updating data file {file_path.name} with AST: {e}", file=sys.stderr)
                print(f"    Please manually check {file_path.name} for corruption.", file=sys.stderr)

    def _on_sdxl_toggled(self, change): self._update_model_lists()
    def _update_model_lists(self):
        with self.layouts['main_output_area']:
            print(f"Updating model lists based on SDXL toggle: {self.widgets['sdxl_toggle'].value}")
            self._save_current_selections()
            is_xl = self.widgets['sdxl_toggle'].value
            models_py_path = ANXETY_ROOT / 'scripts' / ('_xl-models-data.py' if is_xl else '_models-data.py')
            loras_py_path = ANXETY_ROOT / 'scripts' / '_loras-data.py'

            # Define potential new data files
            embeddings_py_path = ANXETY_ROOT / 'scripts' / '_embeddings-data.py'
            hypernetworks_py_path = ANXETY_ROOT / 'scripts' / '_hypernetworks-data.py'


            if not models_py_path.exists(): 
                print(f"    ⚠️ Model data file not found at {models_py_path}. Skipping model list update.", file=sys.stderr); return
            
            models_data = runpy.run_path(str(models_py_path))
            loras_data = runpy.run_path(str(loras_py_path))
            
            # Check for and load new data files if they exist
            embeddings_data = runpy.run_path(str(embeddings_py_path)) if embeddings_py_path.exists() else {}
            hypernetworks_data = runpy.run_path(str(hypernetworks_py_path)) if hypernetworks_py_path.exists() else {}


            data_map = {'model_list': models_data.get('sdxl_models_data' if is_xl else 'sd15_model_data', {}),
                        'vae_list': models_data.get('sdxl_vae_data' if is_xl else 'sd15_vae_data', {}),
                        'controlnet_list': models_data.get('controlnet_list', {}),
                        'lora_list': loras_data.get('lora_data', {}).get('sdxl_loras' if is_xl else 'sd15_loras', {}),
                        'embedding_list': embeddings_data.get('sdxl_embeddings' if is_xl else 'sd15_embeddings', {}), # New list
                        'hypernetwork_list': hypernetworks_data.get('sdxl_hypernetworks' if is_xl else 'sd15_hypernetworks', {}) # New list
                        }
            
            # Update layout map for new accordion sections
            layout_map = {'model_list': self.layouts['models_box'], 'vae_list': self.layouts['vaes_box'],
                          'controlnet_list': self.layouts['cnets_box'], 'lora_list': self.layouts['loras_box'],
                          # You'll need to create new VBoxes in _create_layouts and add them to the accordion for these:
                          # 'embedding_list': self.layouts['embeddings_box'],
                          # 'hypernetwork_list': self.layouts['hypernetworks_box']
                          }

            for key, data_dict in data_map.items():
                if key in layout_map: # Only process if a corresponding layout box exists
                    selection_set = self.selections.get(key, set())
                    new_checkboxes = [self.factory.create_checkbox(description=name, value=(name in selection_set)) for name in data_dict.keys()]
                    self.widgets[key] = new_checkboxes
                    layout_map[key].children = tuple(new_checkboxes)
                else:
                    print(f"    ℹ️ Skipping list update for '{key}': No corresponding layout box defined.", file=sys.stderr)


    def _save_current_selections(self):
        with self.layouts['main_output_area']:
            print("Saving current checkbox selections...")
            for key in self.selections.keys():
                if key in self.widgets and isinstance(self.widgets[key], list):
                    for checkbox in self.widgets[key]:
                        if checkbox.value: self.selections[key].add(checkbox.description)
                        else: self.selections[key].discard(checkbox.description)
            print("Selections saved to internal state.")
        
    def on_launch_click(self, b):
        b.description = "Processing..."; b.icon = "spinner"; b.disabled = True
        with self.layouts['main_output_area']:
            clear_output(wait=True)
            print("--- Initiating Launch Sequence ---")
            self.save_settings()
            print("\n--- 2. Running Environment Setup (VENV & Assets) ---")
            # Ensure this call doesn't re-launch UI
            get_ipython().run_line_magic('run', str(ANXETY_ROOT / 'scripts' / 'en' / 'downloading-en.py'))
            print("\n--- 3. Launching WebUI ---")
            get_ipython().run_line_magic('run', str(ANXETY_ROOT / 'scripts' / 'launch.py'))
        b.description = "Launch Complete"; b.icon = "check"; b.disabled = False
        
    def save_settings(self):
        with self.layouts['main_output_area']:
            print("--- 1. Saving All UI Settings ---")
            self._save_current_selections()
            SETTINGS_PATH = ANXETY_ROOT / 'settings.json'
            widget_values = {key: list(value) for key, value in self.selections.items()}
            # Also save direct widget values not part of selections
            widget_values.update({
                'detailed_download': self.widgets['detailed_download'].value,
                'change_webui': self.widgets['change_webui'].value,
                'commandline_arguments': self.widgets['commandline_arguments'].value,
                # Save the current URLs in the pool
                'downloader_url_pool_content': self.widgets['downloader_url_pool'].value
            })

            # Example: Save Ngrok token if you add it to widgets
            # if 'ngrok_token' in self.widgets:
            #    widget_values['ngrok_token'] = self.widgets['ngrok_token'].value

            js.save(str(SETTINGS_PATH), 'WIDGETS', widget_values)
            js.save(str(SETTINGS_PATH), 'ENVIRONMENT.home_path', '/content') # Explicitly set home path
            update_current_webui(widget_values['change_webui']) # Update selected WebUI in settings.json
            print("✅ Configuration saved to settings.json")

if __name__ == "__main__":
    ui = AnxietyUI()
    ui.create_ui()

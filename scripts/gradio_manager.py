# /content/ANXETY/scripts/gradio_manager.py (Full Custom Downloader Implementation)

import gradio as gr
from pathlib import Path
import sys
import os
import json
import time
import ast
import re
from functools import partial # For passing arguments to event handlers

# --- Pathing & Imports ---
ANXETY_ROOT = Path('/content/ANXETY')
if str(ANXETY_ROOT) not in sys.path: sys.path.insert(0, str(ANXETY_ROOT))
if str(ANXETY_ROOT / 'modules') not in sys.path: sys.path.insert(0, str(ANXETY_ROOT / 'modules'))

from modules.CivitaiAPI import CivitAiAPI
import modules.json_utils as js

# --- Global/Shared Variables (for Gradio app state) ---
url_pool = []
processed_data = [] # Stores data after API calls for review
civitai_api_instance = None # Will be initialized once

# These will store the dynamically created Gradio components for the review stage
# We'll use a dictionary where keys are original item indices and values are dicts of components
dynamic_review_components = {} 

# --- Helper Functions (copied/adapted from widgets_en.py) ---

def initialize_api():
    """Initializes CivitaiAPI with the token from settings.json."""
    global civitai_api_instance
    if civitai_api_instance is None:
        try:
            settings_path = ANXETY_ROOT / 'settings.json'
            civitai_token = js.read(settings_path, 'WIDGETS.civitai_token', None)
            civitai_api_instance = CivitAiAPI(civitai_token)
            return "✅ Civitai API initialized."
        except Exception as e:
            return f"❌ Error initializing Civitai API: {e}"
    return "✅ Civitai API already initialized."


def _get_huggingface_guesses(url):
    """Guesses asset details for Hugging Face URLs."""
    try:
        filename = url.split('/')[-1].split('?')[0]
        file_type = "Checkpoint"; base_model = "Unknown"
        
        if any(ext in filename.lower() for ext in ['.safetensors', '.ckpt', '.pt', '.bin']):
            if "lora" in filename.lower(): file_type = "LORA"
            elif "vae" in filename.lower(): file_type = "VAE"
            elif "control" in filename.lower(): file_type = "ControlNet"
            elif "embed" in filename.lower() or "textualinversion" in filename.lower(): file_type = "Embedding"
            elif "hypernetwork" in filename.lower(): file_type = "Hypernetwork"
            else: file_type = "Checkpoint"
        
        if "sdxl" in filename.lower() or "xl" in url.lower(): base_model = "SDXL 1.0"
        elif "pony" in filename.lower(): base_model = "Pony"
        elif "1.5" in filename.lower() or "1-5" in url.lower(): base_model = "SD 1.5"
        else: base_model = "Unknown"

        guessed_name = filename.rsplit('.', 1)[0]
        download_url_clean = url.replace("/blob/", "/resolve/").split('?')[0] 

        return {'source': 'HuggingFace', 'name': guessed_name, 'type': file_type, 'baseModel': base_model, 'files': [{'name': filename, 'downloadUrl': download_url_clean}]}
    except Exception as e:
        print(f"Error guessing HF details for {url}: {e}", file=sys.stderr)
        return None

def _categorize_and_write(data, asset_type, base_model, display_name, file_name, download_url):
    """Categorizes and writes new model entry to data files using AST."""
    target_file, target_dict = None, None
    is_sdxl_type = 'SDXL' in base_model or 'Pony' in base_model 

    print(f"  Categorizing: '{display_name}' (Type: {asset_type}, Base: {base_model})")

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
        target_file = ANXETY_ROOT / 'scripts' / ('_xl-models-data.py' if is_sdxl_type else '_models-data.py') # Assuming controlnets may live in XL files
        target_dict = 'controlnet_list' 
    elif asset_type in ['Embedding', 'TextualInversion']: 
        target_file = ANXETY_ROOT / 'scripts' / '_embeddings-data.py' 
        target_dict = 'sdxl_embeddings' if is_sdxl_type else 'sd15_embeddings'
    elif asset_type == 'Hypernetwork':
        target_file = ANXETY_ROOT / 'scripts' / '_hypernetworks-data.py' 
        target_dict = 'sdxl_hypernetworks' if is_sdxl_type else 'sd15_hypernetworks'
    elif asset_type == 'Other': 
        target_file = ANXETY_ROOT / 'scripts' / ('_xl-models-data.py' if is_sdxl_type else '_models-data.py')
        target_dict = 'other_assets' 

    if not target_file or not target_dict: 
        print(f"    ⚠️ Could not categorize model '{display_name}'. Skipping writing to data file.", file=sys.stderr); 
        return "Failed to categorize asset."

    new_entry = {'display_name': display_name, 'url': download_url, 'filename': file_name}
    print(f"    Attempting to write new entry to {target_file.name}, dictionary '{target_dict}'.")
    return _update_data_file_with_ast(target_file, target_dict, new_entry, asset_type)

def _update_data_file_with_ast(file_path, dict_name, new_entry, asset_type):
    """Updates Python data file using AST."""
    if not file_path.exists():
        print(f"    Creating new data file: {file_path.name}")
        initial_content = ""
        if file_path.name == '_loras-data.py':
            initial_content = f"lora_data = {{'sd15_loras': {{}}, 'sdxl_loras': {{}}}}\n"
        elif file_path.name == '_embeddings-data.py':
            initial_content = f"sd15_embeddings = {{}}\nsdxl_embeddings = {{}}\n"
        elif file_path.name == '_hypernetworks-data.py':
            initial_content = f"sd15_hypernetworks = {{}}\nsdxl_hypernetworks = {{}}\n"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(initial_content)
        print(f"    Initialized {file_path.name} with basic structure.")

    try:
        with open(file_path, 'r', encoding='utf-8') as f: 
            source_code = f.read()
        tree = ast.parse(source_code)
        found_and_modified = False

        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == dict_name:
                        dict_node = node.value
                        if isinstance(dict_node, ast.Dict):
                            if any(isinstance(k, ast.Constant) and k.value == new_entry['display_name'] for k in dict_node.keys):
                                print(f"    ℹ️ '{asset_type}' '{new_entry['display_name']}' already exists in {dict_name}. Skipping addition.")
                                found_and_modified = True
                                break
                            
                            key_node = ast.Constant(value=new_entry['display_name'])
                            value_node = ast.Dict(keys=[ast.Constant(value='url'), ast.Constant(value='name')], 
                                                  values=[ast.Constant(value=new_entry['url']), ast.Constant(value=new_entry['filename'])])
                            
                            dict_node.keys.append(key_node)
                            dict_node.values.append(value_node)
                            found_and_modified = True
                            print(f"    Successfully added '{new_entry['display_name']}' to '{dict_name}' in '{file_path.name}'.")
                            break 
                if found_and_modified:
                    break 
            elif file_path.name == '_loras-data.py' and isinstance(node, ast.Assign) and hasattr(node.targets[0], 'id') and node.targets[0].id == 'lora_data':
                for i, key in enumerate(node.value.keys):
                    if isinstance(key, ast.Constant) and key.value == dict_name:
                        dict_node = node.value.values[i]
                        if isinstance(dict_node, ast.Dict):
                            if any(isinstance(k, ast.Constant) and k.value == new_entry['display_name'] for k in dict_node.keys):
                                print(f"    ℹ️ LoRA '{new_entry['display_name']}' already exists. Skipping."); found_and_modified = True; break
                            key_node = ast.Constant(value=new_entry['display_name'])
                            value_node = ast.Dict(keys=[ast.Constant(value='url'), ast.Constant(value='name')], values=[ast.Constant(value=new_entry['url']), ast.Constant(value=new_entry['filename'])])
                            dict_node.keys.append(key_node); dict_node.values.append(value_node); found_and_modified = True; break
                if found_and_modified: break

        if not found_and_modified: 
            print(f"    ❌ Error: Could not find dictionary '{dict_name}' or add '{new_entry['display_name']}' in {file_path}. Please check data file format and target dictionary name.", file=sys.stderr); return "Failed to update data file."
        
        new_source_code = ast.unparse(tree)
        with open(file_path, 'w', encoding='utf-8') as f: 
            f.write(new_source_code)
        return f"✅ Successfully updated {file_path.name} for {new_entry['display_name']}."
    except Exception as e:
        print(f"    ❌ Critical Error updating data file {file_path.name} with AST: {e}", file=sys.stderr)
        return f"❌ Critical Error updating data file: {e}"


# --- Gradio UI Functions ---

def add_urls_to_pool(urls_input):
    """Adds URLs from the input text area to the pool."""
    global url_pool
    new_urls_raw = urls_input.strip()
    if not new_urls_raw:
        return "", "ℹ️ No URLs provided to add." # Return empty string for urls_input
    
    new_urls = [url.strip() for line in new_urls_raw.splitlines() for url in line.split(',') if url.strip()]
    
    added_count = 0
    for url in new_urls:
        if url and url not in url_pool:
            url_pool.append(url)
            added_count += 1
    
    return "\n".join(url_pool), f"✅ Added {added_count} new URLs. Total: {len(url_pool)}."

def process_and_display_review_stage(urls_input_text_area): # Pass urls_input_text_area here
    """Processes URLs and returns Gradio components for the review stage."""
    global processed_data, url_pool, dynamic_review_components

    # Update url_pool from the text area in case user manually edited it
    url_pool = [url.strip() for line in urls_input_text_area.splitlines() for url in line.split(',') if url.strip()]

    if not civitai_api_instance:
        return gr.Column(visible=False), gr.Column(visible=False), gr.Markdown.update(visible=True, value="❌ Civitai API not initialized. Check console for errors."), [], gr.JSON().update(value={}) # Update signature

    if not url_pool:
        return gr.Column(visible=True), gr.Column(visible=False), gr.Markdown.update(visible=True, value="⚠️ URL Pool is empty. Please add URLs first."), [], gr.JSON().update(value={}) # Update signature

    processed_data = []
    messages = ["--- Starting Data Fetch for URLs ---", "Fetching data for URLs. This might take a moment..."]
    messages.append(f"URLs in pool: {url_pool}")

    for url_index, url in enumerate(url_pool):
        # Gradio progress bar update
        # progress((url_index / len(url_pool), "Processing URLs..."), desc=f"Processing URL {url_index + 1}/{len(url_pool)}")
        messages.append(f"\n  Processing URL {url_index + 1}/{len(url_pool)}: {url}")
        data = None
        try:
            if "civitai.com" in url:
                messages.append(f"    Detected Civitai URL. Calling CivitAiAPI.get_model...")
                data = civitai_api_instance.get_model(url)
                if data:
                    messages.append(f"    Civitai API returned data for: {data.name} (Type: {data.type})")
                else:
                    messages.append(f"    Civitai API returned no data or failed for {url}. This might happen for unsupported Civitai URLs (e.g., direct download links instead of model pages).")
            elif "huggingface.co" in url:
                messages.append(f"    Detected Hugging Face URL. Guessing asset type...")
                data = _get_huggingface_guesses(url)
                if data:
                    messages.append(f"    Guessed HF data for: {data.get('name')} (Type: {data.get('type')})")
                else:
                    messages.append(f"    Hugging Face guessing failed for {url}.")
            else:
                messages.append(f"    Unsupported URL type: {url}. Skipping.")

            if data: 
                processed_data.append(data)
                messages.append(f"    URL successfully processed and added to processed_data.")
            else:
                messages.append(f"    ⚠️ Skipping {url} due to no data or unsupported format.")
        except Exception as e:
            messages.append(f"    ❌ An unexpected error occurred while processing {url}: {e}")
            print(f"Error processing {url}: {e}", file=sys.stderr) # Also print to console for deeper debug

    if not processed_data:
        messages.append("\n❌ No valid model data could be retrieved from the provided URLs. Please check URLs and try again.")
        return gr.Column(visible=True), gr.Column(visible=False), gr.Markdown.update(value="\n".join(messages)), [], gr.JSON().update(value={}) # Update signature

    messages.append(f"\nSuccessfully processed {len(processed_data)} URLs. Building review UI.")
    type_order = {'Checkpoint': 0, 'LORA': 1, 'VAE': 2, 'ControlNet': 3, 'Embedding': 4, 'TextualInversion': 4, 'Hypernetwork': 5, 'Other': 99} 
    processed_data.sort(key=lambda x: (type_order.get(x.type if hasattr(x, 'type') else x.get('type', 'Unknown'), 99), x.name if hasattr(x, 'name') else x.get('name', '')))

    review_components_list = [] # List of Gradio components to be returned for display
    dynamic_review_components.clear() # Clear previous state

    messages.append(f"Preparing {len(processed_data)} items for review panel.")
    for i, item in enumerate(processed_data):
        item_key = str(i) # Use string key for dictionary
        messages.append(f"  Item {item_key}: Name='{item.name if hasattr(item, 'name') else item.get('name', 'Unknown')}', Type='{item.type if hasattr(item, 'type') else item.get('type', 'Unknown')}'")
        is_hf = isinstance(item, dict)
        name = item.get('name') if is_hf else item.name
        source = item.get('source', 'Civitai') if is_hf else 'Civitai'
        
        # Gradio components for this item
        current_item_widgets = {}

        name_label = gr.Markdown(f"### {name} ({source})", elem_classes=["review-item-header"])
        review_components_list.append(name_label)
        current_item_widgets["name_label"] = name_label # Store reference

        type_options = ['Checkpoint', 'LORA', 'VAE', 'ControlNet', 'Embedding', 'TextualInversion', 'Hypernetwork', 'Other'] 
        type_val = item.get('type') if is_hf else item.type
        if type_val not in type_options: type_val = 'Other' 
        type_dropdown = gr.Dropdown(type_options, value=type_val, label="Asset Type", interactive=True)
        review_components_list.append(type_dropdown)
        current_item_widgets["type_dropdown"] = type_dropdown # Store reference
        
        base_model_options = ['SD 1.5', 'SDXL 1.0', 'Pony', 'Unknown', 'Other'] 
        base_model_val = item.get('baseModel') if is_hf else (item.model_versions[0].base_model if hasattr(item, 'model_versions') and item.model_versions else 'Unknown')
        if base_model_val not in base_model_options: base_model_val = 'Other'
        base_model_dropdown = gr.Dropdown(base_model_options, value=base_model_val, label="Base Model", interactive=True)
        review_components_list.append(base_model_dropdown)
        current_item_widgets["base_model_dropdown"] = base_model_dropdown # Store reference

        file_dropdown_options = []
        file_url_map = {}
        selected_file_name = ""
        selected_file_url = ""

        if not is_hf and hasattr(item, 'model_versions') and item.model_versions:
            versions_map = {v.name: v for v in item.model_versions}
            version_names = list(versions_map.keys())
            
            # Initial version files
            if version_names and versions_map[version_names[0]].files:
                file_dropdown_options = {f.name: f.download_url for f in versions_map[version_names[0]].files}
                file_url_map = file_dropdown_options
                if file_dropdown_options:
                    selected_file_name = list(file_dropdown_options.keys())[0]
                    selected_file_url = file_dropdown_options[selected_file_name]

            version_dropdown = gr.Dropdown(version_names, value=version_names[0] if version_names else None, label="Model Version", interactive=True)
            review_components_list.append(version_dropdown)
            current_item_widgets["version_dropdown"] = version_dropdown # Store reference

            # File dropdown for Civitai
            file_dropdown = gr.Dropdown(list(file_dropdown_options.keys()), value=selected_file_name, label="File", interactive=True)
            review_components_list.append(file_dropdown)
            current_item_widgets["file_dropdown"] = file_dropdown # Store reference

            # On version change, update file options dynamically
            # This requires a new Gradio event, which means partial.
            # We need to capture the current `item_id` and the `file_dropdown` instance.
            version_dropdown.change(
                fn=lambda selected_version: (
                    {f.name: f.download_url for f in versions_map.get(selected_version, versions_map.get(version_names[0])).files if hasattr(versions_map.get(selected_version, versions_map.get(version_names[0])), 'files') and versions_map.get(selected_version, versions_map.get(version_names[0])).files},
                    list({f.name: f.download_url for f in versions_map.get(selected_version, versions_map.get(version_names[0])).files if hasattr(versions_map.get(selected_version, versions_map.get(version_names[0])), 'files') and versions_map.get(selected_version, versions_map.get(version_names[0])).files}.keys())
                ),
                inputs=[version_dropdown],
                outputs=[gr.State(), file_dropdown] # Outputting a hidden state for file_url_map and updating file_dropdown options
                , api_name=f"update_files_{item_id}" # Unique API name
            )
            # Update the stored file_url_map and file_selection value when version changes
            # This is complex with Gradio's state. We'll store it in a hidden JSON component.
            # For simplicity, we'll rely on the default selection or first item for now.
        elif is_hf: 
            messages.append("    Hugging Face item: Assuming single file.")
            if item.get('files'):
                file_url_to_use = item['files'][0]['downloadUrl']
                file_name_to_use = item['files'][0]['name']
            else:
                messages.append(f"    No files found for Hugging Face item '{name}'. Skipping from review UI.")
                continue 
            
            # HF items have a fixed file, so use Markdown for display
            file_display_markdown = gr.Markdown(f"**Selected File:** `{file_name_to_use}`\n\n*URL:* `{file_url_to_use}`")
            review_components_list.append(file_display_markdown)
            current_item_widgets["file_display_markdown"] = file_display_markdown # Store reference
            
            # Store the fixed file name and URL for HF items
            current_item_widgets["file_name"] = file_name_to_use
            current_item_widgets["file_url"] = file_url_to_use
        else:
            messages.append(f"    ⚠️ Item '{name}' has no identifiable files. Skipping from review UI.")
            continue 
        
        # Store the collected Gradio component references and their current values (for non-dynamic parts)
        dynamic_review_components[item_key] = current_item_widgets
        
        review_components_list.append(gr.HTML("<hr>")) # Separator

    if not review_components_list: # Check if any items were actually added to review_components_list
        messages.append("❌ No items were successfully prepared for the review stage. Returning to initial view.")
        return gr.Column(visible=True), gr.Column(visible=False), gr.Markdown.update(value="\n".join(messages)), [], gr.JSON().update(value={})

    # Return initial_stage hidden, review_stage visible, messages, and the list of components
    return gr.Column(visible=False), gr.Column(visible=True), gr.Markdown.update(value="\n".join(messages)), review_components_list, gr.JSON(value=dynamic_review_components).update(visible=False)


def final_submit_review(dynamic_review_components_json):
    """Called when the user confirms the review stage."""
    global url_pool
    messages = ["--- Writing Selections to Data Scripts ---"]
    success_count = 0

    # `dynamic_review_components_json` will be the JSON representation of the dynamic_review_components dictionary
    # We need to reconstruct the values from their current states
    
    # Example of how to access values from the JSON:
    # `item_data_from_json` would be a dictionary like:
    # {
    #   "name_label": {"value": "### ModelName (Source)"},
    #   "type_dropdown": "Checkpoint", # This is the selected value
    #   "base_model_dropdown": "SDXL 1.0",
    #   "file_name": "filename.safetensors",
    #   "file_url": "http://download.url"
    # }

    for item_key, item_data_from_json in dynamic_review_components_json.items():
        name = item_data_from_json['name_label']['value'].replace("### ", "").split('(')[0].strip() # Extract name from markdown string
        asset_type_val = item_data_from_json['type_dropdown'] # Directly the selected value
        base_model_val = item_data_from_json['base_model_dropdown'] # Directly the selected value
        file_name = item_data_from_json['file_name']
        download_url = item_data_from_json['file_url']

        messages.append(f"  Processing confirmed item: '{name}' (Type: {asset_type_val}, Base: {base_model_val}, File: {file_name})")
        try:
            result = _categorize_and_write(
                None, # `data` object is not directly used by _categorize_and_write now, can be None
                asset_type_val, 
                base_model_val, 
                name, # display_name
                file_name, 
                download_url
            )
            messages.append(result)
            if "✅" in result:
                success_count += 1
        except Exception as e:
            messages.append(f"    ❌ Error processing item '{name}' for writing: {e}")
            print(f"Error processing item '{name}' for writing: {e}", file=sys.stderr)

    messages.append(f"✅ Processed {success_count} items. Returning to main menu...")
    url_pool = [] # Clear the pool after processing
    # Return to the initial view
    return gr.Column(visible=True), gr.Column(visible=False), gr.Markdown.update(value="\n".join(messages)) # Show initial, hide review


# --- Gradio UI Definition ---

with gr.Blocks(theme=gr.themes.Soft(), css="""
    .gradio-container {
        background-color: #2e2e2e; /* Dark background */
        color: #e0e0e0; /* Light text */
    }
    .gr-button {
        background-color: #555;
        color: #eee;
        border: 1px solid #777;
    }
    .gr-button:hover {
        background-color: #666;
    }
    .review-item-header {
        color: #7289DA; /* Accent color for headers */
    }
    hr {
        border-top: 1px dashed #777;
    }
    .gr-textarea { /* Style for text areas */
        background-color: #1c1c1c !important;
        color: #f0f8ff !important;
        border: 1px solid #262626 !important;
    }
    .gr-dropdown { /* Style for dropdowns */
        background-color: #1c1c1c !important;
        color: #f0f8ff !important;
        border: 1px solid #262626 !important;
    }
    .gr-dropdown-item { /* Style for dropdown items */
        color: #e0e0e0 !important;
    }
""") as demo:
    gr.Markdown("# Anxiety Lightning - Model Manager (Gradio)")
    status_output = gr.Markdown(initialize_api())

    with gr.Column(visible=True) as initial_stage:
        gr.Markdown("## Add New Models/Assets")
        urls_input = gr.Textbox(label="Paste URLs (one per line or comma-separated)", lines=5, placeholder="https://civitai.com/models/xyz\nhttps://huggingface.co/author/repo/file.safetensors")
        add_button = gr.Button("Add to Pool", elem_classes=["button", "button_save"])
        
        current_pool = gr.Textbox(label="Current URL Pool", lines=5, interactive=False)
        process_button = gr.Button("Process & Review URLs", elem_classes=["button", "button_save"])

        # Actions for initial stage
        add_button.click(
            add_urls_to_pool,
            inputs=[urls_input],
            outputs=[current_pool, status_output]
        )

    with gr.Column(visible=False) as review_stage:
        gr.Markdown("## Review & Categorize Detected Assets")
        # This Column will be dynamically populated with review_components_list
        review_items_column = gr.Column() 
        confirm_button = gr.Button("Confirm All and Add to Library", elem_classes=["button", "button_save"], interactive=True)
        
        # Hidden JSON component to pass dynamic_review_components dictionary
        # Its value will be set by process_and_display_review_stage and read by final_submit_review
        hidden_dynamic_components_json = gr.JSON(value={}, visible=False)

    # Re-define process_button.click after review_items_column and hidden_dynamic_components_json are defined
    process_button.click(
        process_and_display_review_stage,
        inputs=[current_pool], # Pass the content of the URL pool Textbox
        outputs=[initial_stage, review_stage, status_output, review_items_column, hidden_dynamic_components_json],
        queue=True # Important for long-running processes
    )

    # Final submit button in the review stage
    confirm_button.click(
        final_submit_review,
        inputs=[hidden_dynamic_components_json], # Pass the hidden JSON data
        outputs=[initial_stage, review_stage, status_output] # Return to initial view
    )

# --- Run the Gradio App ---
# You would call this from your notebook's startup cell, e.g., in launch.py
# Or directly if this is your main entry point.
if __name__ == "__main__":
    demo.launch(debug=True, share=True, quiet=False) # Enable share for public URL in Colab

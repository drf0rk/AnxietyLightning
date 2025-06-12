# /content/ANXETY/scripts/gradio_manager.py (Initial Gradio Manager UI)

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
        target_file = ANXETY_ROOT / 'scripts' / ('_xl-models-data.py' if is_xl_type else '_models-data.py') # Assuming controlnets may live in XL files
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
        return url_pool, "ℹ️ No URLs provided to add."
    
    new_urls = [url.strip() for line in new_urls_raw.splitlines() for url in line.split(',') if url.strip()]
    
    added_count = 0
    for url in new_urls:
        if url and url not in url_pool:
            url_pool.append(url)
            added_count += 1
    
    return "\n".join(url_pool), f"✅ Added {added_count} new URLs. Total: {len(url_pool)}."

def process_and_display_review_stage(progress=gr.Progress()):
    """Processes URLs and returns Gradio components for the review stage."""
    global processed_data, url_pool

    if not civitai_api_instance:
        return gr.Column(visible=False), gr.Column(visible=False), "❌ Civitai API not initialized. Check console for errors."

    if not url_pool:
        return gr.Column(visible=False), gr.Column(visible=False), "⚠️ URL Pool is empty. Please add URLs first."

    processed_data = []
    messages = ["--- Starting Data Fetch for URLs ---", "Fetching data for URLs. This might take a moment..."]
    messages.append(f"URLs in pool: {url_pool}")

    for url_index, url in enumerate(url_pool):
        progress((url_index / len(url_pool), "Processing URLs..."), desc=f"Processing URL {url_index + 1}/{len(url_pool)}")
        messages.append(f"\n  Processing URL {url_index + 1}/{len(url_pool)}: {url}")
        data = None
        try:
            if "civitai.com" in url:
                messages.append(f"    Detected Civitai URL. Calling CivitAiAPI.get_model...")
                data = civitai_api_instance.get_model(url)
                if data:
                    messages.append(f"    Civitai API returned data for: {data.name} (Type: {data.type})")
                else:
                    messages.append(f"    Civitai API returned no data or failed for {url}.")
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
        return gr.Column(visible=True), gr.Column(visible=False), "\n".join(messages)

    messages.append(f"\nSuccessfully processed {len(processed_data)} URLs. Building review UI.")
    type_order = {'Checkpoint': 0, 'LORA': 1, 'VAE': 2, 'ControlNet': 3, 'Embedding': 4, 'TextualInversion': 4, 'Hypernetwork': 5, 'Other': 99} 
    processed_data.sort(key=lambda x: (type_order.get(x.type if hasattr(x, 'type') else x.get('type', 'Unknown'), 99), x.name if hasattr(x, 'name') else x.get('name', '')))

    review_components = []
    # Using a list to hold dictionary of Gradio components for each item
    # This allows retrieving values easily during the final save step
    item_gr_components = [] 

    messages.append(f"Preparing {len(processed_data)} items for review panel.")
    for i, item in enumerate(processed_data):
        item_id = i # Simple ID for referencing in the submit function
        messages.append(f"  Item {item_id+1}: Name='{item.name if hasattr(item, 'name') else item.get('name', 'Unknown')}', Type='{item.type if hasattr(item, 'type') else item.get('type', 'Unknown')}'")
        is_hf = isinstance(item, dict)
        name = item.get('name') if is_hf else item.name
        source = item.get('source', 'Civitai') if is_hf else 'Civitai'
        
        # Name and Source Label
        name_label = gr.Markdown(f"### {name} ({source})", elem_classes=["review-item-header"])
        
        # Asset Type Dropdown
        type_options = ['Checkpoint', 'LORA', 'VAE', 'ControlNet', 'Embedding', 'TextualInversion', 'Hypernetwork', 'Other'] 
        type_val = item.get('type') if is_hf else item.type
        if type_val not in type_options: type_val = 'Other' 
        type_dropdown = gr.Dropdown(type_options, value=type_val, label="Asset Type", interactive=True)
        
        # Base Model Dropdown
        base_model_options = ['SD 1.5', 'SDXL 1.0', 'Pony', 'Unknown', 'Other'] 
        base_model_val = item.get('baseModel') if is_hf else (item.model_versions[0].base_model if hasattr(item, 'model_versions') and item.model_versions else 'Unknown')
        if base_model_val not in base_model_options: base_model_val = 'Other'
        base_model_dropdown = gr.Dropdown(base_model_options, value=base_model_val, label="Base Model", interactive=True)

        # File Selection (Simplified for now - using URL directly)
        file_url_to_use = ""
        file_name_to_use = ""

        if not is_hf and hasattr(item, 'model_versions') and item.model_versions:
            if item.model_versions[0].files:
                file_url_to_use = item.model_versions[0].files[0].download_url
                file_name_to_use = item.model_versions[0].files[0].name
                messages.append(f"    Civitai item: Using first file '{file_name_to_use}' from first version for review.")
            else:
                messages.append(f"    No files found for initial version of Civitai item '{name}'. Skipping from review UI.")
                continue # Skip this item if no downloadable files are found.
        elif is_hf: 
            if item.get('files'):
                file_url_to_use = item['files'][0]['downloadUrl']
                file_name_to_use = item['files'][0]['name']
                messages.append(f"    Hugging Face item: Using first guessed file '{file_name_to_use}' for review.")
            else:
                messages.append(f"    No files found for Hugging Face item '{name}'. Skipping from review UI.")
                continue # Skip this item if no downloadable files are found.
        else:
            messages.append(f"    ⚠️ Item '{name}' has no identifiable files. Skipping from review UI.")
            continue # Skip this item if no downloadable files are found.
        
        file_display_markdown = gr.Markdown(f"**Selected File:** `{file_name_to_use}`\n\n*URL:* `{file_url_to_use}`")
        
        # Store components and their data for final submission
        item_gr_components.append({
            "name_label": name_label,
            "type_dropdown": type_dropdown,
            "base_model_dropdown": base_model_dropdown,
            "file_name": file_name_to_use, # Store the actual name
            "file_url": file_url_to_use # Store the actual URL
        })

        review_components.extend([
            name_label, type_dropdown, base_model_dropdown, file_display_markdown, gr.HTML("<hr>")
        ])

    if not review_components:
        messages.append("❌ No items were successfully prepared for the review stage. Returning to initial view.")
        return gr.Column(visible=True), gr.Column(visible=False), "\n".join(messages)

    # Use a dummy component to hold item_gr_components for the submit function
    # This is a common Gradio pattern to pass complex data between functions
    json_data_store = gr.JSON(item_gr_components, visible=False) # Hide the actual JSON component

    # Create the submit button for this review stage
    submit_button = gr.Button("Confirm & Add to Library", elem_classes=["button", "button_save"], interactive=True)
    
    # Return the components for the review stage, and hide the initial stage
    return gr.Column(visible=False), gr.Column(visible=True), "\n".join(messages)


def final_submit_review(item_gr_components_json):
    """Called when the user confirms the review stage."""
    global url_pool
    messages = ["--- Writing Selections to Data Scripts ---"]
    success_count = 0

    item_gr_components = item_gr_components_json # Data is passed as JSON

    for item_data in item_gr_components:
        name = item_data['name_label']['value'].split('(')[0].strip() # Extract name from markdown string
        try:
            selected_file_name = item_data['file_name']
            download_url = item_data['file_url']

            final_data = {
                'model': {'type': item_data['type_dropdown'], 'name': name}, # Gradio dropdown returns value directly
                'name': selected_file_name.rsplit('.',1)[0],
                'baseModel': item_data['base_model_dropdown'], # Gradio dropdown returns value directly
                'files': [{'name': selected_file_name, 'downloadUrl': download_url}]
            }
            
            result = _categorize_and_write(final_data, final_data['model']['type'], final_data['baseModel'], final_data['model']['name'], selected_file_name, download_url)
            messages.append(result)
            if "✅" in result:
                success_count += 1
        except Exception as e:
            messages.append(f"    ❌ Error processing item '{name}' for writing: {e}")
            print(f"Error processing item '{name}' for writing: {e}", file=sys.stderr)

    messages.append(f"✅ Processed {success_count} items. Returning to main menu...")
    url_pool = [] # Clear the pool after processing
    # Return to the initial view
    return gr.Column(visible=True), gr.Column(visible=False), "\n".join(messages) # Show initial, hide review


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

        process_button.click(
            process_and_display_review_stage,
            inputs=[],
            outputs=[initial_stage, gr.Column(visible=False), status_output], # Output is complex, will be updated below
            queue=True # Important for long-running processes
        )

    with gr.Column(visible=False) as review_stage:
        gr.Markdown("## Review & Categorize Detected Assets")
        review_output_area = gr.Markdown() # To display individual item details
        confirm_button = gr.Button("Confirm All and Add to Library", elem_classes=["button", "button_save"])

        # The actual components for review are built dynamically and returned by process_and_display_review_stage
        # We need a placeholder for them. Let's make it more generic.
        # This is where the output of process_and_display_review_stage will go.
        # We also need to capture the item_gr_components_json to pass to final_submit_review
        
        # Dummy component to hold item_gr_components for the submit function
        item_gr_components_json_placeholder = gr.JSON(value=[], visible=False)

        # Update the process_button.click output to include the dynamically created review components
        process_button.click(
            process_and_display_review_stage,
            inputs=[],
            outputs=[initial_stage, review_stage, status_output, item_gr_components_json_placeholder], # Need to output the JSON data store
            queue=True # Important for long-running processes
        )
        # This part of the Gradio interface will be dynamically populated by process_and_display_review_stage
        # Let's make it a general Column for the review items.
        review_items_column = gr.Column()
        
        # After process_and_display_review_stage runs, it should dynamically update review_items_column
        # This requires process_and_display_review_stage to return a list of components which can be added
        # to a gr.Column, or to create them and assign them directly to the review_items_column if possible.
        # For a more robust approach in Gradio, it's better to update the children of a gr.Column directly.
        # So, the process_and_display_review_stage will return gr.update for the review_items_column's children.

        # Let's rethink the process_and_display_review_stage output.
        # It needs to return (initial_stage_visibility, review_stage_visibility, status_message, review_items_content, item_gr_components_json)
        # And the confirm_button needs to access item_gr_components_json

    # Redefining process_button.click for clarity
    process_button.click(
        process_and_display_review_stage,
        inputs=[],
        outputs=[initial_stage, review_stage, status_output, review_items_column, item_gr_components_json_placeholder],
        queue=True
    ).success(
        # This is a placeholder for the actual dynamic display.
        # In Gradio, dynamically adding widgets can be complex.
        # A common pattern is to use gr.Dataset or gr.DataFrame,
        # or have pre-defined slots that get populated.
        # For now, let's just make sure the `review_stage` is visible and the output message is clear.
        # The actual `review_items_column` will need to be populated within `process_and_display_review_stage`
        # or via a chained event that returns the list of components.
        lambda initial, review, status, items_json: (gr.Column(visible=initial), gr.Column(visible=review), gr.Markdown(status),
                                                    # Need to dynamically create components here based on items_json
                                                    # Or return the component list directly from process_and_display_review_stage
                                                    # For simplicity, let's have process_and_display_review_stage return the review_items_column as children
                                                    gr.update(children=[
                                                        gr.Markdown(f"### {item['name_label']['value']}"),
                                                        gr.Dropdown(item['type_dropdown']['choices'], value=item['type_dropdown']['value'], label="Asset Type"),
                                                        gr.Dropdown(item['base_model_dropdown']['choices'], value=item['base_model_dropdown']['value'], label="Base Model"),
                                                        gr.Markdown(f"**Selected File:** `{item['file_name']}`\n\n*URL:* `{item['file_url']}`"),
                                                        gr.HTML("<hr>")
                                                    for item in items_json]), # THIS IS PSEUDOCODE - Gradio needs actual components not just markdown/strings
                                                    gr.JSON(items_json, visible=False) # Keep JSON data for next step
                                                   )
        , # This is where the complex part is. Gradio's state management for dynamic component lists is tricky.
        # For now, let's keep the `process_and_display_review_stage` simpler in its return
        # and rely on it setting the `review_stage` visibility.
        # The content for `review_items_column` will need to be generated by `process_and_display_review_stage`
        # which means it needs to *return* the actual Gradio components, not just text.
    )


    # Final submit button in the review stage
    confirm_button.click(
        final_submit_review,
        inputs=[item_gr_components_json_placeholder], # Pass the hidden JSON data
        outputs=[initial_stage, review_stage, status_output] # Return to initial view
    )


# --- Run the Gradio App ---
# You would call this from your notebook's startup cell, e.g., in launch.py
# Or directly if this is your main entry point.
if __name__ == "__main__":
    demo.launch(debug=True, share=True, quiet=False) # Enable share for public URL in Colab

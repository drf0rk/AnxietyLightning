# /content/ANXETY/scripts/gradio_setup_ui.py

import gradio as gr
import sys
import runpy
from pathlib import Path
import subprocess
import shlex
import time

# --- Pathing & Imports ---
# This ensures the script can find the project's modules
try:
    ANXETY_ROOT = Path(__file__).resolve().parents[1]
except NameError:
    ANXETY_ROOT = Path('/content/ANXETY') # Fallback for some environments

if str(ANXETY_ROOT) not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT))
if str(ANXETY_ROOT / 'modules') not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT / 'modules'))

import modules.json_utils as js
from modules.webui_utils import update_current_webui

# --- Data Loading ---
# Execute the data files to load their dictionaries into memory
try:
    sd15_data = runpy.run_path(str(ANXETY_ROOT / 'scripts/_models-data.py'))
    sdxl_data = runpy.run_path(str(ANXETY_ROOT / 'scripts/_xl-models-data.py'))
    loras_data_full = runpy.run_path(str(ANXETY_ROOT / 'scripts/_loras-data.py'))

    # Extract choices for the UI CheckboxGroups
    sd15_model_choices = list(sd15_data.get('sd15_model_data', {}).keys())
    sd15_vae_choices = list(sd15_data.get('sd15_vae_data', {}).keys())
    
    sdxl_model_choices = list(sdxl_data.get('sdxl_models_data', {}).keys())
    sdxl_vae_choices = list(sdxl_data.get('sdxl_vae_data', {}).keys())

    sd15_lora_choices = list(loras_data_full.get('lora_data', {}).get('sd15_loras', {}).keys())
    sdxl_lora_choices = list(loras_data_full.get('lora_data', {}).get('sdxl_loras', {}).keys())
    
    # ControlNets are often shared or specific to a base model version
    controlnet_choices = list(sd15_data.get('controlnet_list', {}).keys())
    
except Exception as e:
    print(f"FATAL ERROR: Could not load data files. Please ensure _models-data.py, _xl-models-data.py, and _loras-data.py exist and are valid. Error: {e}")
    sys.exit(1)


webui_selection_args = {
    'A1111': "--xformers --no-half-vae --enable-insecure-extension-access --disable-console-progressbars --theme dark",
    'ComfyUI': "--use-sage-attention --dont-print-server",
    'Forge': "--disable-xformers --opt-sdp-attention --cuda-stream --pin-shared-memory --enable-insecure-extension-access --disable-console-progressbars --theme dark",
    'Classic': "--persistent-patches --cuda-stream --pin-shared-memory --enable-insecure-extension-access --disable-console-progressbars --theme dark",
    'ReForge': "--xformers --cuda-stream --pin-shared-memory --enable-insecure-extension-access --disable-console-progressbars --theme dark",
    'SD-UX': "--xformers --no-half-vae --enable-insecure-extension-access --disable-console-progressbars --theme dark"
}

# --- Core Logic Function ---
def save_and_launch(webui_choice, is_sdxl, selected_models, selected_vaes, selected_loras, selected_cnets, launch_args, ngrok_token, detailed_download):
    """Gathers all UI selections, saves them to settings.json, and runs the backend."""
    
    # 1. Yield initial status
    yield "✅ UI selections received. Preparing to save settings..."
    
    # 2. Construct the settings dictionary
    settings_data = {
        'WIDGETS': {
            'change_webui': webui_choice,
            'XL_models': is_sdxl, # This is a new key, the backend will need to adapt or we can remove it. Let's keep for now.
            'model_list': selected_models or [],
            'vae_list': selected_vaes or [],
            'lora_list': selected_loras or [],
            'controlnet_list': selected_cnets or [],
            'commandline_arguments': launch_args or "",
            'ngrok_token': ngrok_token or "",
            'detailed_download': detailed_download
        },
        'ENVIRONMENT': {
            'home_path': '/content'
        }
    }
    
    # 3. Save to settings.json
    settings_path = ANXETY_ROOT / 'settings.json'
    js.save(str(settings_path), 'WIDGETS', settings_data['WIDGETS'])
    js.save(str(settings_path), 'ENVIRONMENT', settings_data['ENVIRONMENT'])
    update_current_webui(webui_choice) # This sets up the WEBUI section of the JSON
    
    yield "✅ Settings saved to settings.json. Starting backend setup..."
    time.sleep(1)

    # 4. Execute backend scripts and stream output
    scripts_to_run = [
        ANXETY_ROOT / 'scripts' / 'en' / 'downloading-en.py',
        ANXETY_ROOT / 'scripts' / 'launch.py'
    ]

    full_output = "✅ Settings saved to settings.json. Starting backend setup..."
    for script_path in scripts_to_run:
        full_output += f"\n\n--- 🚀 Running {script_path.name} ---\n"
        yield full_output
        
        try:
            process = subprocess.Popen(
                [sys.executable, str(script_path)],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding='utf-8',
                errors='replace'
            )
            
            for line in iter(process.stdout.readline, ''):
                full_output += line
                yield full_output
            
            process.stdout.close()
            process.wait()
            if process.returncode != 0:
                full_output += f"\n--- ❌ ERROR: {script_path.name} exited with code {process.returncode} ---\n"
                yield full_output
                break # Stop execution if a script fails
        except Exception as e:
            full_output += f"\n--- ❌ CRITICAL FAILURE running {script_path.name}: {e} ---\n"
            yield full_output
            break
            
    full_output += "\n--- ✅ Process Complete ---"
    yield full_output

# --- Gradio UI Definition ---
with gr.Blocks(theme=gr.themes.Soft(primary_hue="purple", secondary_hue="blue"), css=".gradio-container {background-color: #1a1a1a; padding: 20px;}") as demo:
    gr.Markdown("# AnxietyLightning Setup")
    gr.Markdown("Configure your Stable Diffusion environment, select assets, and launch the WebUI.")

    with gr.Row():
        with gr.Column(scale=2):
            webui_dropdown = gr.Dropdown(choices=['ReForge', 'Forge', 'A1111', 'ComfyUI', 'Classic', 'SD-UX'], value='ReForge', label="1. Select WebUI")
        with gr.Column(scale=1, min_width=200):
            sdxl_toggle = gr.Checkbox(label="Use SDXL Models", value=False)
    
    with gr.Accordion("2. Asset Selection", open=True):
        with gr.Tab("Models & VAEs"):
            with gr.Row():
                model_checkboxes = gr.CheckboxGroup(choices=sd15_model_choices, label="Checkpoints")
                vae_checkboxes = gr.CheckboxGroup(choices=sd15_vae_choices, label="VAEs")
        with gr.Tab("LoRAs & ControlNets"):
            with gr.Row():
                lora_checkboxes = gr.CheckboxGroup(choices=sd15_lora_choices, label="LoRAs")
                controlnet_checkboxes = gr.CheckboxGroup(choices=controlnet_choices, label="ControlNets")
    
    with gr.Accordion("3. Advanced Options", open=False):
        args_textbox = gr.Textbox(label="Commandline Arguments", value=webui_selection_args['ReForge'], lines=2)
        ngrok_textbox = gr.Textbox(label="NGROK Token (Optional)", type="password")
        detailed_dl_checkbox = gr.Checkbox(label="Show Detailed Download Logs", value=False)
        
    # Launch Button and Output Log
    launch_button = gr.Button("Install, Download & Launch", variant="primary", scale=2)
    output_log = gr.Textbox(label="Live Log", interactive=False, lines=25, max_lines=50)

    # --- UI Interactions ---
    def update_asset_choices(is_sdxl):
        models = sdxl_model_choices if is_sdxl else sd15_model_choices
        vaes = sdxl_vae_choices if is_sdxl else sd15_vae_choices
        loras = sdxl_lora_choices if is_sdxl else sd15_lora_choices
        # ControlNets might also change, but for now we assume they are shared or XL specific
        return gr.update(choices=models, value=[]), gr.update(choices=vaes, value=[]), gr.update(choices=loras, value=[])

    sdxl_toggle.change(
        fn=update_asset_choices, 
        inputs=sdxl_toggle, 
        outputs=[model_checkboxes, vae_checkboxes, lora_checkboxes]
    )
    
    def update_args(webui_choice):
        return gr.update(value=webui_selection_args.get(webui_choice, ""))
        
    webui_dropdown.change(fn=update_args, inputs=webui_dropdown, outputs=args_textbox)

    # Main launch action
    launch_button.click(
        fn=save_and_launch,
        inputs=[
            webui_dropdown,
            sdxl_toggle,
            model_checkboxes,
            vae_checkboxes,
            lora_checkboxes,
            controlnet_checkboxes,
            args_textbox,
            ngrok_textbox,
            detailed_dl_checkbox
        ],
        outputs=output_log
    )

if __name__ == "__main__":
    # share=False because launch.py will create the final public tunnels for the SD WebUI
    demo.launch(share=False)

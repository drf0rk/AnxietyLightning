# /content/ANXETY/scripts/gradio_setup_ui.py

import gradio as gr
import sys
import runpy
from pathlib import Path
import subprocess
import shlex

# --- Pathing & Imports ---
ANXETY_ROOT = Path('/content/ANXETY')
if str(ANXETY_ROOT) not in sys.path: sys.path.insert(0, str(ANXETY_ROOT))
import modules.json_utils as js
from modules.webui_utils import update_current_webui

# --- Data Loading ---
# Load model/lora/vae options from the data files
sd15_models_data = runpy.run_path(str(ANXETY_ROOT / 'scripts/_models-data.py'))
sdxl_models_data = runpy.run_path(str(ANXETY_ROOT / 'scripts/_xl-models-data.py'))
loras_data = runpy.run_path(str(ANXETY_ROOT / 'scripts/_loras-data.py'))

# Extract choices for the UI
sd15_model_choices = list(sd15_models_data.get('sd15_model_data', {}).keys())
sdxl_model_choices = list(sdxl_models_data.get('sdxl_models_data', {}).keys())
# ... and so on for VAEs and LoRAs

webui_selection_args = {
    'ReForge': "--xformers --cuda-stream ...",
    'Forge': "--disable-xformers --opt-sdp-attention ...",
    # ... etc
}

# --- Core Logic Function ---
def save_and_launch(*args):
    """Gathers all UI selections, saves them to settings.json, and runs the backend."""
    
    # 1. Unpack all arguments from the Gradio components
    # The order must match the .click(inputs=[...]) list
    webui_choice, is_sdxl, selected_models, selected_loras, launch_args, ngrok_token = args
    
    # 2. Construct the settings dictionary
    settings_data = {
        'WIDGETS': {
            'change_webui': webui_choice,
            'XL_models': is_sdxl,
            'model_list': selected_models,
            'lora_list': selected_loras,
            'commandline_arguments': launch_args,
            'ngrok_token': ngrok_token
            # ... add other settings like vae_list, controlnet_list, etc.
        },
        'ENVIRONMENT': {
            'home_path': '/content'
        }
    }
    
    # 3. Save to settings.json
    settings_path = ANXETY_ROOT / 'settings.json'
    js.save(str(settings_path), 'WIDGETS', settings_data['WIDGETS'])
    js.save(str(settings_path), 'ENVIRONMENT', settings_data['ENVIRONMENT'])
    update_current_webui(webui_choice)
    
    yield "✅ Settings saved to settings.json. Starting backend setup..."

    # 4. Execute backend scripts and stream output
    scripts_to_run = [
        ANXETY_ROOT / 'scripts' / 'en' / 'downloading-en.py',
        ANXETY_ROOT / 'scripts' / 'launch.py'
    ]

    for script_path in scripts_to_run:
        yield f"\n--- 🚀 Running {script_path.name} ---"
        process = subprocess.Popen(
            [sys.executable, str(script_path)],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding='utf-8',
            errors='replace'
        )
        
        full_output = ""
        for line in iter(process.stdout.readline, ''):
            full_output += line
            yield full_output
        
        process.stdout.close()
        process.wait()
        
    yield "\n--- ✅ Process Complete ---"


# --- Gradio UI Definition ---
with gr.Blocks(theme=gr.themes.Soft(), css=".gradio-container {background-color: #1a1a1a}") as demo:
    gr.Markdown("# AnxietyLightning Setup")
    gr.Markdown("Configure your Stable Diffusion environment and launch.")

    with gr.Row():
        webui_dropdown = gr.Dropdown(choices=['ReForge', 'Forge', 'A1111', 'ComfyUI'], value='ReForge', label="Select WebUI")
        sdxl_toggle = gr.Checkbox(label="Use SDXL Models", value=False)
    
    with gr.Accordion("Asset Selection", open=True):
        model_checkboxes = gr.CheckboxGroup(choices=sd15_model_choices, label="Checkpoints")
        lora_checkboxes = gr.CheckboxGroup(choices=loras_data.get('lora_data').get('sd15_loras').keys(), label="LoRAs")
        # Add more CheckboxGroups for VAEs, ControlNets etc.

    with gr.Accordion("Advanced Options", open=False):
        args_textbox = gr.Textbox(label="Commandline Arguments", value=webui_selection_args['ReForge'])
        ngrok_textbox = gr.Textbox(label="NGROK Token (Optional)", type="password")
        
    # Launch Button and Output Log
    launch_button = gr.Button("Install, Download & Launch", variant="primary")
    output_log = gr.Textbox(label="Live Log", interactive=False, lines=20)

    # --- UI Interactions ---
    # Update model choices when SDXL toggle changes
    def update_model_choices(is_sdxl):
        choices = sdxl_model_choices if is_sdxl else sd15_model_choices
        return gr.update(choices=choices, value=[]) # Reset selection

    sdxl_toggle.change(fn=update_model_choices, inputs=sdxl_toggle, outputs=model_checkboxes)
    
    # Update launch args when WebUI changes
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
            lora_checkboxes,
            args_textbox,
            ngrok_textbox
        ],
        outputs=output_log
    )

if __name__ == "__main__":
    demo.launch(share=False) # Share=False because launch.py will handle public tunnels

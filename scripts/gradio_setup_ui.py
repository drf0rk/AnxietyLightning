# /content/ANXETY/scripts/gradio_setup_ui.py (v1.3 - Public Share Enabled)

import gradio as gr
import sys
import runpy
from pathlib import Path
import subprocess
import shlex
import time

# --- Pathing & Imports ---
try:
    ANXETY_ROOT = Path(__file__).resolve().parents[1]
except NameError:
    ANXETY_ROOT = Path('/content/ANXETY')

if str(ANXETY_ROOT) not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT))

from modules import json_utils as js
from modules.webui_utils import update_current_webui

# --- Data Loading ---
try:
    sd15_data = runpy.run_path(str(ANXETY_ROOT / 'scripts/_models-data.py'))
    sdxl_data = runpy.run_path(str(ANXETY_ROOT / 'scripts/_xl-models-data.py'))
    loras_data_full = runpy.run_path(str(ANXETY_ROOT / 'scripts/_loras-data.py'))

    sd15_model_choices = list(sd15_data.get('sd15_model_data', {}).keys())
    sd15_vae_choices = list(sd15_data.get('sd15_vae_data', {}).keys())
    sdxl_model_choices = list(sdxl_data.get('sdxl_models_data', {}).keys())
    sdxl_vae_choices = list(sdxl_data.get('sdxl_vae_data', {}).keys())
    sd15_lora_choices = list(loras_data_full.get('lora_data', {}).get('sd15_loras', {}).keys())
    sdxl_lora_choices = list(loras_data_full.get('lora_data', {}).get('sdxl_loras', {}).keys())
    controlnet_choices = list(sd15_data.get('controlnet_list', {}).keys())
except Exception as e:
    print(f"FATAL ERROR: Could not load data files. Error: {e}")
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
    yield "✅ UI selections received. Saving settings..."
    settings_data = {
        'WIDGETS': {
            'change_webui': webui_choice, 'XL_models': is_sdxl, 'model_list': selected_models or [],
            'vae_list': selected_vaes or [], 'lora_list': selected_loras or [], 'controlnet_list': selected_cnets or [],
            'commandline_arguments': launch_args or "", 'ngrok_token': ngrok_token or "", 'detailed_download': detailed_download
        }, 'ENVIRONMENT': {'home_path': '/content'}
    }
    settings_path = ANXETY_ROOT / 'settings.json'
    js.save(str(settings_path), 'WIDGETS', settings_data['WIDGETS'])
    js.save(str(settings_path), 'ENVIRONMENT', settings_data['ENVIRONMENT'])
    update_current_webui(webui_choice)
    full_output = "✅ Settings saved. Starting backend setup...\n(You can monitor the full process here.)"
    yield full_output
    time.sleep(1)
    scripts_to_run = [ANXETY_ROOT/'scripts'/'en'/'downloading-en.py', ANXETY_ROOT/'scripts'/'launch.py']
    for script_path in scripts_to_run:
        full_output += f"\n\n--- 🚀 Running {script_path.name} ---\n"
        yield full_output
        try:
            process = subprocess.Popen([sys.executable, str(script_path)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8', errors='replace')
            for line in iter(process.stdout.readline, ''):
                full_output += line
                yield full_output
            process.stdout.close()
            process.wait()
            if process.returncode != 0:
                full_output += f"\n--- ❌ ERROR: {script_path.name} exited with code {process.returncode} ---\n"; yield full_output; break
        except Exception as e:
            full_output += f"\n--- ❌ CRITICAL FAILURE running {script_path.name}: {e} ---\n"; yield full_output; break
    full_output += "\n--- ✅ Process Complete ---"
    yield full_output

# --- Gradio UI Definition ---
with gr.Blocks(theme=gr.themes.Soft(primary_hue="purple", secondary_hue="blue"), css=".gradio-container {background-color: #1a1a1a; padding: 20px;}") as demo:
    gr.Markdown("# AnxietyLightning Setup")
    
    with gr.Tabs() as tabs:
        with gr.TabItem("1. Setup & Asset Selection", id=0):
            gr.Markdown("Configure your Stable Diffusion environment and select assets to download.")
            with gr.Row():
                with gr.Column(scale=2):
                    webui_dropdown = gr.Dropdown(choices=['ReForge', 'Forge', 'A1111', 'ComfyUI', 'Classic', 'SD-UX'], value='ReForge', label="Select WebUI")
                with gr.Column(scale=1, min_width=200):
                    sdxl_toggle = gr.Checkbox(label="Use SDXL Models", value=False)
            with gr.Accordion("Asset Selection", open=True):
                with gr.Row():
                    model_checkboxes = gr.CheckboxGroup(choices=sd15_model_choices, label="Checkpoints", interactive=True)
                    vae_checkboxes = gr.CheckboxGroup(choices=sd15_vae_choices, label="VAEs", interactive=True)
                with gr.Row():
                    lora_checkboxes = gr.CheckboxGroup(choices=sd15_lora_choices, label="LoRAs", interactive=True)
                    controlnet_checkboxes = gr.CheckboxGroup(choices=controlnet_choices, label="ControlNets", interactive=True)
            with gr.Accordion("Advanced Options", open=False):
                args_textbox = gr.Textbox(label="Commandline Arguments", value=webui_selection_args['ReForge'], lines=2, interactive=True)
                with gr.Row():
                    ngrok_textbox = gr.Textbox(label="NGROK Token (Optional)", type="password", scale=3)
                    detailed_dl_checkbox = gr.Checkbox(label="Show Detailed Download Logs", value=False, scale=1)

        with gr.TabItem("2. Launch & Live Log", id=1):
            gr.Markdown("Click the button to begin the setup process. Progress will be displayed below.")
            launch_button = gr.Button("Install, Download & Launch", variant="primary")
            output_log = gr.Textbox(label="Live Log", interactive=False, lines=25, max_lines=50)

    # --- UI Interactions ---
    def update_asset_choices(is_sdxl):
        models = sdxl_model_choices if is_sdxl else sd15_model_choices
        vaes = sdxl_vae_choices if is_sdxl else sd15_vae_choices
        loras = sdxl_lora_choices if is_sdxl else sd15_lora_choices
        return gr.update(choices=models, value=[]), gr.update(choices=vaes, value=[]), gr.update(choices=loras, value=[])

    sdxl_toggle.change(fn=update_asset_choices, inputs=sdxl_toggle, outputs=[model_checkboxes, vae_checkboxes, lora_checkboxes])
    
    def update_args(webui_choice):
        return gr.update(value=webui_selection_args.get(webui_choice, ""))
        
    webui_dropdown.change(fn=update_args, inputs=webui_dropdown, outputs=args_textbox)

    launch_button.click(
        fn=save_and_launch,
        inputs=[
            webui_dropdown, sdxl_toggle, model_checkboxes, vae_checkboxes,
            lora_checkboxes, controlnet_checkboxes, args_textbox, ngrok_textbox, detailed_dl_checkbox
        ],
        outputs=output_log
    )

if __name__ == "__main__":
    demo.launch(share=True)

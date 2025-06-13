# /content/ANXETY/scripts/gradio_setup_ui.py (v1.8 - Enhanced Logging & UI Logic)

import gradio as gr
import sys
import runpy
from pathlib import Path
import subprocess
import shlex
import time
import html

# --- 1. CSS for Modern Logging and UI Styling ---
# This is the "Export" of the style. You can copy this block.
MODERN_LOG_CSS = """
<style>
#log_output_html {
    background-color: #0d1117;
    border: 1px solid #30363d;
    border-radius: 8px;
    padding: 12px;
    font-family: 'Monaco', 'Consolas', 'Menlo', monospace;
    color: #c9d1d9;
    height: 400px; /* Or adjust as needed */
    overflow-y: auto; /* Enable scrolling */
}
#log_output_html .log-line {
    display: block;
    animation: fadeIn 0.5s ease-in-out;
}
#log_output_html .log-header {
    color: #58a6ff;
    font-weight: bold;
    margin-top: 15px;
    margin-bottom: 5px;
    text-shadow: 0 0 5px rgba(88, 166, 255, 0.3);
}
#log_output_html .log-success {
    color: #3fb950;
}
#log_output_html .log-error {
    color: #f85149;
    font-weight: bold;
}
#log_output_html .log-download {
    color: #8b949e;
    font-size: 0.85em;
}
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(5px); }
    to { opacity: 1; transform: translateY(0); }
}
</style>
"""

# --- 2. Pathing, Imports, and Data Loading (Unchanged) ---
try:
    ANXETY_ROOT = Path(__file__).resolve().parents[1]
except NameError:
    ANXETY_ROOT = Path('/content/ANXETY')

if str(ANXETY_ROOT) not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT))

from modules import json_utils as js
from modules.webui_utils import update_current_webui

try:
    sd15_data = runpy.run_path(str(ANXETY_ROOT / 'scripts/_models-data.py'))
    sdxl_data = runpy.run_path(str(ANXETY_ROOT / 'scripts/_xl-models-data.py'))
    loras_data_full = runpy.run_path(str(ANXETY_ROOT / 'scripts/_loras-data.py'))

    sd15_model_choices = list(sd15_data.get('sd15_model_data', {}).keys())
    sd15_vae_choices = list(sd15_data.get('sd15_vae_data', {}).keys())
    sd15_controlnet_choices = list(sd15_data.get('controlnet_list', {}).keys())
    sd15_lora_choices = list(loras_data_full.get('lora_data', {}).get('sd15_loras', {}).keys())
    
    sdxl_model_choices = list(sdxl_data.get('sdxl_models_data', {}).keys())
    sdxl_vae_choices = list(sdxl_data.get('sdxl_vae_data', {}).keys())
    sdxl_controlnet_choices = list(sdxl_data.get('controlnet_list', {}).keys())
    sdxl_lora_choices = list(loras_data_full.get('lora_data', {}).get('sdxl_loras', {}).keys())
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

# --- 3. Core Logic Function (Modified for HTML Logging) ---
def save_and_launch(webui_choice, is_sdxl, selected_models, selected_vaes, selected_loras, selected_cnets, launch_args, ngrok_token, detailed_download):
    
    # Helper to format log lines into HTML
    def format_log_line(line):
        line = html.escape(line)
        if "---" in line:
            return f'<span class="log-line log-header">{line}</span>'
        elif "✅" in line:
            return f'<span class="log-line log-success">{line}</span>'
        elif "❌" in line:
            return f'<span class="log-line log-error">{line}</span>'
        elif "[#" in line and ("MiB/s" in line or "GiB/s" in line):
             return f'<span class="log-line log-download">{line}</span>'
        return f'<span class="log-line">{line}</span>'

    # Initial setup
    yield format_log_line("✅ UI selections received. Saving settings...")
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
    
    full_html_output = format_log_line("✅ Settings saved. Starting backend setup...")
    yield full_html_output
    time.sleep(1)

    # Execute backend scripts
    scripts_to_run = [ANXETY_ROOT/'scripts'/'en'/'downloading-en.py', ANXETY_ROOT/'scripts'/'launch.py']
    for script_path in scripts_to_run:
        full_html_output += format_log_line(f"\n--- 🚀 Running {script_path.name} ---")
        yield full_html_output
        try:
            process = subprocess.Popen([sys.executable, str(script_path)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8', errors='replace')
            for line in iter(process.stdout.readline, ''):
                full_html_output += format_log_line(line.strip())
                yield full_html_output
            process.stdout.close()
            process.wait()
            if process.returncode != 0:
                full_html_output += format_log_line(f"--- ❌ ERROR: {script_path.name} exited with code {process.returncode} ---"); yield full_html_output; break
        except Exception as e:
            full_html_output += format_log_line(f"--- ❌ CRITICAL FAILURE running {script_path.name}: {e} ---"); yield full_html_output; break
            
    full_html_output += format_log_line("\n--- ✅ Process Complete ---")
    yield full_html_output

# --- 4. Gradio UI Definition (The "Exportable" Layout) ---
with gr.Blocks(theme=gr.themes.Soft(primary_hue="purple", secondary_hue="blue"), css=MODERN_LOG_CSS) as demo:
    gr.Markdown("# AnxietyLightning Setup")
    
    with gr.Tabs():
        with gr.TabItem("1. Setup & Asset Selection", id=0):
            # ... (Layout is the same)
            with gr.Row():
                webui_dropdown = gr.Dropdown(choices=['ReForge', 'Forge', 'A1111', 'ComfyUI', 'Classic', 'SD-UX'], value='ReForge', label="Select WebUI")
                sdxl_toggle = gr.Checkbox(label="Use SDXL Models", value=False)
            with gr.Accordion("Asset Selection", open=True):
                with gr.Row():
                    model_checkboxes = gr.CheckboxGroup(choices=sd15_model_choices, label="Checkpoints", interactive=True)
                    vae_checkboxes = gr.CheckboxGroup(choices=sd15_vae_choices, label="VAEs", interactive=True)
                with gr.Row():
                    lora_checkboxes = gr.CheckboxGroup(choices=sd15_lora_choices, label="LoRAs", interactive=True)
                    controlnet_checkboxes = gr.CheckboxGroup(choices=sd15_controlnet_choices, label="ControlNets", interactive=True)
            with gr.Accordion("Advanced Options", open=False):
                args_textbox = gr.Textbox(label="Commandline Arguments", value=webui_selection_args['ReForge'], lines=2, interactive=True)
                with gr.Row():
                    ngrok_textbox = gr.Textbox(label="NGROK Token", type="password", scale=3)
                    detailed_dl_checkbox = gr.Checkbox(label="Detailed Logs", value=False, scale=1)

        with gr.TabItem("2. Launch & Live Log", id=1):
            gr.Markdown("Click the button to begin the setup process. Progress will be displayed below.")
            launch_button = gr.Button("Install, Download & Launch", variant="primary")
            # Changed to gr.HTML for styled output
            output_log = gr.HTML(label="Live Log", elem_id="log_output_html")

    # --- 5. UI Interactions (Corrected Logic) ---
    def update_asset_choices(is_sdxl):
        models = sdxl_model_choices if is_sdxl else sd15_model_choices
        vaes = sdxl_vae_choices if is_sdxl else sd15_vae_choices
        loras = sdxl_lora_choices if is_sdxl else sd15_lora_choices
        # FIX: Also update ControlNets
        cnets = sdxl_controlnet_choices if is_sdxl else sd15_controlnet_choices
        return [
            gr.update(choices=models, value=[]),
            gr.update(choices=vaes, value=[]),
            gr.update(choices=loras, value=[]),
            gr.update(choices=cnets, value=[]) # Reset selection
        ]

    # FIX: Added controlnet_checkboxes to the outputs list
    sdxl_toggle.change(
        fn=update_asset_choices,
        inputs=sdxl_toggle,
        outputs=[model_checkboxes, vae_checkboxes, lora_checkboxes, controlnet_checkboxes]
    )
    
    def update_args(webui_choice):
        return gr.update(value=webui_selection_args.get(webui_choice, ""))
        
    webui_dropdown.change(fn=update_args, inputs=webui_dropdown, outputs=args_textbox)

    launch_button.click(
        fn=save_and_launch,
        inputs=[
            webui_dropdown, sdxl_toggle, model_checkboxes, vae_checkboxes,
            loras_checkboxes, controlnet_checkboxes, args_textbox, ngrok_textbox, detailed_dl_checkbox
        ],
        outputs=output_log
    )

demo.launch(share=True, inline=False)

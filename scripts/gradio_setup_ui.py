# /content/ANXETY/scripts/gradio_setup_ui.py (v5.5 - Final Tuple Yield Fix)

import gradio as gr
import sys
import runpy
from pathlib import Path
import subprocess
import shlex
import time
import html
import re
import logging

# --- Setup Paths & Logger ---
ANXETY_ROOT = Path('/content/ANXETY')
LOG_DIR = ANXETY_ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s', handlers=[logging.FileHandler(LOG_DIR / "gradio_launch.log", mode='w'), logging.StreamHandler(sys.stdout)])

# --- Imports & Data Loading ---
if str(ANXETY_ROOT) not in sys.path: sys.path.insert(0, str(ANXETY_ROOT))
from modules import json_utils as js
from modules.webui_utils import update_current_webui
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
webui_selection_args = {'A1111': "--xformers --no-half-vae", 'Forge': "--disable-xformers --opt-sdp-attention", 'ReForge': "--xformers --cuda-stream", 'Classic': "--persistent-patches --cuda-stream", 'ComfyUI': "--use-sage-attention", 'SD-UX': "--xformers --no-half-vae"}
MODERN_LOG_CSS="""<style>/* CSS content... */</style>"""

def save_and_launch(webui_choice, is_sdxl, selected_models, selected_vaes, selected_loras, selected_cnets, launch_args, ngrok_token, detailed_download):
    """Core logic function, now using tuple-based yield."""
    progress_regex = re.compile(r"\((\d{1,3})%\)")
    def format_log_line(line):
        line = html.escape(line)
        if "---" in line: return f'<span class="log-line log-header">{line}</span>'
        if "✅" in line: return f'<span class="log-line log-success">{line}</span>'
        if "❌" in line: return f'<span class="log-line log-error">{line}</span>'
        if "[#" in line and ("MiB/s" in line or "GiB/s" in line): return f'<span class="log-line log-download">{line}</span>'
        return f'<span class="log-line">{line}</span>'

    # Yield a tuple: (update for output_log, update for download_progress)
    yield (format_log_line("✅ UI selections received. Saving settings..."), gr.update(value=0, visible=True))
    
    settings_data = {
        'WIDGETS': {
            'change_webui': webui_choice, 'sdxl_toggle': is_sdxl, 'model_list': selected_models or [],
            'vae_list': selected_vaes or [], 'lora_list': selected_loras or [], 'controlnet_list': selected_cnets or [],
            'commandline_arguments': launch_args or "", 'ngrok_token': ngrok_token or "", 'detailed_download': detailed_download
        }, 'ENVIRONMENT': {'home_path': '/content'}
    }
    settings_path = ANXETY_ROOT / 'settings.json'
    js.save(str(settings_path), 'WIDGETS', settings_data['WIDGETS'])
    js.save(str(settings_path), 'ENVIRONMENT', settings_data['ENVIRONMENT'])
    update_current_webui(webui_choice)
    full_html_output = format_log_line("✅ Settings saved. Starting backend setup...")
    
    yield (full_html_output, gr.update(visible=False))
    time.sleep(1)

    scripts_to_run = [ANXETY_ROOT/'scripts'/'en'/'downloading-en.py', ANXETY_ROOT/'scripts'/'launch.py']
    for script_path in scripts_to_run:
        full_html_output += format_log_line(f"\n--- 🚀 Running {script_path.name} ---")
        yield (full_html_output, gr.update(value=0, visible=False))
        try:
            process = subprocess.Popen([sys.executable, str(script_path)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8', errors='replace')
            for line in iter(process.stdout.readline, ''):
                clean_line = line.strip()
                progress_update = gr.update()
                if match := progress_regex.search(clean_line):
                    percent = int(match.group(1)) / 100.0
                    progress_update = gr.update(value=percent, visible=True)
                if "Download Results" in clean_line or "Status Legend" in clean_line:
                    progress_update = gr.update(visible=False)
                
                full_html_output += format_log_line(clean_line)
                yield (full_html_output, progress_update)
            process.wait()
        except Exception as e:
             full_html_output += format_log_line(f"--- ❌ CRITICAL FAILURE: {e} ---")
             yield (full_html_output, gr.update(visible=False))
             break
    full_html_output += format_log_line("\n--- ✅ Process Complete ---")
    yield (full_html_output, gr.update(visible=False))

# --- UI Definition ---
with gr.Blocks(theme=gr.themes.Soft(), css=MODERN_LOG_CSS) as demo:
    with gr.Tabs():
        with gr.TabItem("1. Setup & Asset Selection"):
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
        with gr.TabItem("2. Launch & Live Log"):
            download_progress = gr.Progress()
            launch_button = gr.Button("Install, Download & Launch", variant="primary")
            output_log = gr.HTML(label="Live Log", elem_id="log_output_html")

    # --- UI Interactions ---
    def update_asset_choices(is_sdxl):
        models, vaes, loras, cnets = (sdxl_model_choices, sdxl_vae_choices, sdxl_lora_choices, sdxl_controlnet_choices) if is_sdxl else (sd15_model_choices, sd15_vae_choices, sd15_lora_choices, sd15_controlnet_choices)
        return [gr.update(choices=models, value=[]), gr.update(choices=vaes, value=[]), gr.update(choices=loras, value=[]), gr.update(choices=cnets, value=[])]
    def update_args(webui_choice): return gr.update(value=webui_selection_args.get(webui_choice, ""))
    
    sdxl_toggle.change(fn=update_asset_choices, inputs=sdxl_toggle, outputs=[model_checkboxes, vae_checkboxes, lora_checkboxes, controlnet_checkboxes])
    webui_dropdown.change(fn=update_args, inputs=webui_dropdown, outputs=args_textbox)
    
    # The `outputs` list now correctly maps to the tuple yielded by `save_and_launch`
    launch_button.click(
        fn=save_and_launch, 
        inputs=[webui_dropdown, sdxl_toggle, model_checkboxes, vae_checkboxes, lora_checkboxes, controlnet_checkboxes, args_textbox, ngrok_textbox, detailed_dl_checkbox], 
        outputs=[output_log, download_progress]
    )

demo.launch(share=True, inline=False)

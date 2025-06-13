# /content/ANXETY/scripts/gradio_setup_ui.py (v6.0 - Lazy Load Edition)

import gradio as gr
import sys
import runpy
from pathlib import Path
import subprocess
import shlex
import time
import html
import re
import json
import logging

# --- Setup Paths & Logger ---
ANXETY_ROOT = Path('/content/ANXETY')
LOG_DIR = ANXETY_ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s', handlers=[logging.FileHandler(LOG_DIR / "gradio_launch.log", mode='w'), logging.StreamHandler(sys.stdout)])
logger = logging.getLogger(__name__)

# --- Imports & Data Loading (for initial state) ---
if str(ANXETY_ROOT) not in sys.path: sys.path.insert(0, str(ANXETY_ROOT))
from modules import json_utils as js
from modules.webui_utils import update_current_webui

logger.info("Loading initial data sets...")
sd15_data = runpy.run_path(str(ANXETY_ROOT / 'scripts/_models-data.py'))
sdxl_data = runpy.run_path(str(ANXETY_ROOT / 'scripts/_xl-models-data.py'))
loras_data_full = runpy.run_path(str(ANXETY_ROOT / 'scripts/_loras-data.py'))

# Default choices (SD 1.5) for instant UI load
sd15_model_choices = list(sd15_data.get('sd15_model_data', {}).keys())
sd15_vae_choices = list(sd15_data.get('sd15_vae_data', {}).keys())
sd15_controlnet_choices = list(sd15_data.get('controlnet_list', {}).keys())
sd15_lora_choices = list(loras_data_full.get('lora_data', {}).get('sd15_loras', {}).keys())
logger.info("Initial (SD 1.5) choices loaded.")

webui_selection_args = {'A1111':"--xformers --no-half-vae",'Forge':"--disable-xformers --opt-sdp-attention",'ReForge':"--xformers --cuda-stream",'Classic':"--persistent-patches --cuda-stream",'ComfyUI':"--use-sage-attention",'SD-UX':"--xformers --no-half-vae"}
MODERN_LOG_CSS="""<style>#log_output_html{background-color:#0d1117;border:1px solid #30363d;border-radius:8px;padding:12px;font-family:'Monaco','Consolas','Menlo',monospace;color:#c9d1d9;height:400px;overflow-y:auto}#log_output_html .log-line{display:block;animation:fadeIn .5s ease-in-out}#log_output_html .log-header{color:#58a6ff;font-weight:700;margin-top:15px;margin-bottom:5px;text-shadow:0 0 5px rgba(88,166,255,.3)}#log_output_html .log-success{color:#3fb950}#log_output_html .log-error{color:#f85149;font-weight:700}#log_output_html .log-url{color:#9e87ff;font-weight:700}#log_output_html .log-download{color:#8b949e;font-size:.85em}@keyframes fadeIn{from{opacity:0;transform:translateY(5px)}to{opacity:1;transform:translateY(0)}}</style>"""

def _serialize_settings_to_json(webui_choice, is_sdxl, selected_models, selected_vaes, selected_loras, selected_cnets, launch_args, ngrok_token, detailed_download):
    settings_data = {'WIDGETS':{'change_webui':webui_choice,'sdxl_toggle':is_sdxl,'model_list':selected_models or [],'vae_list':selected_vaes or [],'lora_list':selected_loras or [],'controlnet_list':selected_cnets or [],'commandline_arguments':launch_args or "",'ngrok_token':ngrok_token or "",'detailed_download':detailed_download},'ENVIRONMENT':{'home_path':'/content'}}
    settings_path = ANXETY_ROOT / 'settings.json'
    js.save(str(settings_path), 'WIDGETS', settings_data['WIDGETS'])
    js.save(str(settings_path), 'ENVIRONMENT', settings_data['ENVIRONMENT'])
    update_current_webui(webui_choice)

def _format_log_entry(log_entry):
    level = log_entry.get('level', 'info')
    message = html.escape(log_entry.get('message', ''))
    return f'<span class="log-line log-{level}">{message}</span>'

def _stream_backend_script(script_path, initial_html=""):
    full_html_output = initial_html
    try:
        process = subprocess.Popen([sys.executable, str(script_path)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8', errors='replace')
        for line in iter(process.stdout.readline, ''):
            clean_line = line.strip()
            if not clean_line: continue
            accordion_update = gr.update()
            try:
                log_entry = json.loads(clean_line)
                full_html_output += _format_log_entry(log_entry)
                if log_entry.get('level') == 'progress':
                    percentage = log_entry.get('data', {}).get('percentage', 0)
                    accordion_update = gr.update(label=f"Status: {log_entry.get('message', 'Downloading...')} {percentage}%")
            except json.JSONDecodeError:
                full_html_output += f'<span class="log-line">{html.escape(clean_line)}</span>'
            yield (full_html_output, accordion_update)
        process.wait()
    except Exception as e:
        error_message = f"--- ❌ CRITICAL FAILURE in {script_path.name}: {e} ---"
        full_html_output += f'<span class="log-line log-error">{html.escape(error_message)}</span>'
        yield (full_html_output, gr.update(label="Status: ❌ CRITICAL FAILURE"))

def save_and_launch(webui_choice, is_sdxl, selected_models, selected_vaes, selected_loras, selected_cnets, launch_args, ngrok_token, detailed_download):
    _serialize_settings_to_json(webui_choice, is_sdxl, selected_models, selected_vaes, selected_loras, selected_cnets, launch_args, ngrok_token, detailed_download)
    html_log = _format_log_entry({'level': 'success', 'message': 'Settings saved. Starting backend setup...'})
    yield (html_log, gr.update(label="Status: Starting Backend..."))
    time.sleep(1)

    downloader_streamer = _stream_backend_script(ANXETY_ROOT/'scripts'/'en'/'downloading-en.py', html_log)
    for html_log, accordion_update in downloader_streamer: yield (html_log, accordion_update)
        
    launch_streamer = _stream_backend_script(ANXETY_ROOT/'scripts'/'launch.py', html_log)
    for html_log, accordion_update in launch_streamer: yield (html_log, accordion_update)

    final_log = html_log + _format_log_entry({'level': 'success', 'message': '--- ✅ Process Complete ---'})
    yield (final_log, gr.update(label="Status: ✅ Process Complete"))

with gr.Blocks(theme=gr.themes.Soft(), css=MODERN_LOG_CSS) as demo:
    with gr.Tabs():
        with gr.TabItem("1. Setup & Asset Selection"):
            with gr.Row():
                webui_dropdown = gr.Dropdown(choices=['ReForge', 'Forge', 'A1111', 'ComfyUI', 'Classic', 'SD-UX'], value='ReForge', label="Select WebUI")
                sdxl_toggle = gr.Checkbox(label="Use SDXL Models", value=False)
            with gr.Accordion("Asset Selection", open=True):
                with gr.Row():
                    # Initialize with default data for a fast launch
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
            launch_button = gr.Button("Install, Download & Launch", variant="primary")
            with gr.Accordion("Live Log", open=True) as log_accordion:
                output_log = gr.HTML(label="Live Log", elem_id="log_output_html")

    def update_asset_choices(is_sdxl):
        logger.info(f"Dynamically reloading data for is_sdxl={is_sdxl}")
        sd_data = runpy.run_path(str(ANXETY_ROOT / 'scripts' / ('_xl-models-data.py' if is_sdxl else '_models-data.py')))
        loras_data_full = runpy.run_path(str(ANXETY_ROOT / 'scripts/_loras-data.py'))
        
        models = list(sd_data.get('sdxl_models_data' if is_sdxl else 'sd15_model_data', {}).keys())
        vaes = list(sd_data.get('sdxl_vae_data' if is_sdxl else 'sd15_vae_data', {}).keys())
        loras = list(loras_data_full.get('lora_data', {}).get('sdxl_loras' if is_sdxl else 'sd15_loras', {}).keys())
        cnets = list(sd_data.get('controlnet_list', {}).keys())
        
        return [gr.update(choices=models, value=[]), gr.update(choices=vaes, value=[]), gr.update(choices=loras, value=[]), gr.update(choices=cnets, value=[])]
    
    def update_args(webui_choice): return gr.update(value=webui_selection_args.get(webui_choice, ""))
    
    sdxl_toggle.change(fn=update_asset_choices, inputs=sdxl_toggle, outputs=[model_checkboxes, vae_checkboxes, lora_checkboxes, controlnet_checkboxes])
    webui_dropdown.change(fn=update_args, inputs=webui_dropdown, outputs=args_textbox)
    launch_button.click(fn=save_and_launch, inputs=[webui_dropdown, sdxl_toggle, model_checkboxes, vae_checkboxes, lora_checkboxes, controlnet_checkboxes, args_textbox, ngrok_textbox, detailed_dl_checkbox], outputs=[output_log, log_accordion])
    
    # FINAL FIX: Remove the demo.load() event.
    # The UI will now launch instantly with the default SD1.5 data.

if __name__ == "__main__":
    logger.info("Gradio script starting...")
    ngrok_token_from_arg = sys.argv[1] if len(sys.argv) > 1 else ""
    if ngrok_token_from_arg:
        js.save(str(ANXETY_ROOT / 'settings.json'), 'WIDGETS.ngrok_token', ngrok_token_from_arg)
        logger.info("NGROK token received from command line and pre-saved.")
    demo.launch(share=True, inline=False)

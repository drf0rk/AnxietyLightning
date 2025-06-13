# /content/ANXETY/scripts/gradio_setup_ui.py (v6.2 - Self-Contained)

import gradio as gr
import sys
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
logging.basicConfig(level=logging.INFO, format='[%(levelname)s - %(asctime)s] %(message)s', handlers=[logging.FileHandler(LOG_DIR / "gradio_launch.log", mode='w'), logging.StreamHandler(sys.stdout)])
logger = logging.getLogger(__name__)

# --- Imports & Lightweight Setup ---
if str(ANXETY_ROOT) not in sys.path: sys.path.insert(0, str(ANXETY_ROOT))
from modules import json_utils as js
from modules.webui_utils import update_current_webui

# --- ROBUSTNESS FIX: Hardcoded Data Choices ---
# This eliminates all runpy calls and external file dependencies, which are the source of the hang.
logger.info("Using hardcoded data for maximum stability.")
sd15_model_choices = ["Counterfeit-V3.0", "epicPorn-v1", "Anything-v5"]
sd15_vae_choices = ["vae-ft-mse-840000-ema-pruned", "clearvae_v23"]
sd15_lora_choices = ["Detail Tweaker", "Good Hands", "epiCPhotoGasm"]
sd15_controlnet_choices = ["control_v11p_sd15_openpose", "control_v11f1p_sd15_depth"]

sdxl_model_choices = ["dreamshaper-xl-v2-turbo", "juggernaut-xl-v9", "realvis-xl-v4"]
sdxl_vae_choices = ["sdxl_vae", "madebyollin_sdxl_vae"]
sdxl_lora_choices = ["sdxl_film_photography", "sdxl_detail_slider"]
sdxl_controlnet_choices = ["T2I-Adapter-XL-canny", "T2I-Adapter-XL-depth-zoe"]
# ---

webui_selection_args = {'A1111':"--xformers --no-half-vae",'Forge':"--disable-xformers --opt-sdp-attention",'ReForge':"--xformers --cuda-stream",'Classic':"--persistent-patches --cuda-stream",'ComfyUI':"--use-sage-attention",'SD-UX':"--xformers --no-half-vae"}
MODERN_LOG_CSS="""<style>/* CSS content... */</style>""" # Omitted for brevity

# --- Backend Functions (Remain Unchanged) ---
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

# --- UI Definition and Events ---
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
            launch_button = gr.Button("Install, Download & Launch", variant="primary")
            with gr.Accordion("Live Log", open=True) as log_accordion:
                output_log = gr.HTML(label="Live Log", elem_id="log_output_html")

    def update_asset_choices(is_sdxl):
        logger.info(f"Using hardcoded choices for is_sdxl={is_sdxl}")
        models, vaes, loras, cnets = (sdxl_model_choices, sdxl_vae_choices, sdxl_lora_choices, sdxl_controlnet_choices) if is_sdxl else (sd15_model_choices, sd15_vae_choices, sd15_lora_choices, sd15_controlnet_choices)
        return [gr.update(choices=models, value=[]), gr.update(choices=vaes, value=[]), gr.update(choices=loras, value=[]), gr.update(choices=cnets, value=[])]
    
    def update_args(webui_choice): return gr.update(value=webui_selection_args.get(webui_choice, ""))
    
    sdxl_toggle.change(fn=update_asset_choices, inputs=sdxl_toggle, outputs=[model_checkboxes, vae_checkboxes, lora_checkboxes, controlnet_checkboxes])
    webui_dropdown.change(fn=update_args, inputs=webui_dropdown, outputs=args_textbox)
    launch_button.click(fn=save_and_launch, inputs=[webui_dropdown, sdxl_toggle, model_checkboxes, vae_checkboxes, lora_checkboxes, controlnet_checkboxes, args_textbox, ngrok_textbox, detailed_dl_checkbox], outputs=[output_log, log_accordion])
    
    # demo.load is no longer needed as the initial choices are hardcoded.

if __name__ == "__main__":
    logger.info("Self-Contained Gradio script starting...")
    ngrok_token_from_arg = sys.argv[1] if len(sys.argv) > 1 else ""
    if ngrok_token_from_arg:
        js.save(str(ANXETY_ROOT / 'settings.json'), 'WIDGETS.ngrok_token', ngrok_token_from_arg)
        logger.info("NGROK token received from command line and pre-saved.")
    
    demo.launch(share=True, inline=False)

# /content/ANXETY/scripts/gradio_setup_ui.py (v7.0 - Bulletproof Edition)

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

# --- Hardcoded Data for Maximum Stability ---
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
MODERN_LOG_CSS="""<style>#log_output_html{background-color:#0d1117;border:1px solid #30363d;border-radius:8px;padding:12px;font-family:'Monaco','Consolas','Menlo',monospace;color:#c9d1d9;height:400px;overflow-y:auto}#log_output_html .log-line{display:block;animation:fadeIn .5s ease-in-out}#log_output_html .log-header{color:#58a6ff;font-weight:700;margin-top:15px;margin-bottom:5px;text-shadow:0 0 5px rgba(88,166,255,.3)}#log_output_html .log-success{color:#3fb950}#log_output_html .log-error{color:#f85149;font-weight:700}#log_output_html .log-url{color:#9e87ff;font-weight:700}#log_output_html .log-download{color:#8b949e;font-size:.85em}@keyframes fadeIn{from{opacity:0;transform:translateY(5px)}to{opacity:1;transform:translateY(0)}}</style>"""

def _serialize_settings_to_json(webui_choice, is_sdxl, selected_models, selected_vaes, selected_loras, selected_cnets, launch_args, ngrok_token, detailed_download):
    settings_data = {'WIDGETS':{'change_webui':webui_choice,'sdxl_toggle':is_sdxl,'model_list':selected_models or [],'vae_list':selected_vaes or [],'lora_list':selected_loras or [],'controlnet_list':selected_cnets or [],'commandline_arguments':launch_args or "",'ngrok_token':ngrok_token or "",'detailed_download':detailed_download},'ENVIRONMENT':{'home_path':'/content'}}
    settings_path = ANXETY_ROOT / 'settings.json'
    js.save(str(settings_path), 'WIDGETS', settings_data['WIDGETS'])
    js.save(str(settings_path), 'ENVIRONMENT', settings_data['ENVIRONMENT'])
    update_current_webui(webui_choice)

def save_and_launch(webui_choice, is_sdxl, selected_models, selected_vaes, selected_loras, selected_cnets, launch_args, ngrok_token, detailed_download):
    _serialize_settings_to_json(webui_choice, is_sdxl, selected_models, selected_vaes, selected_loras, selected_cnets, launch_args, ngrok_token, detailed_download)
    full_html_output = '<span class="log-line log-success">✅ Settings saved. Starting backend setup...</span>'
    yield full_html_output
    time.sleep(1)

    scripts_to_run = [ANXETY_ROOT/'scripts'/'en'/'downloading-en.py', ANXETY_ROOT/'scripts'/'launch.py']
    for script_path in scripts_to_run:
        full_html_output += f'<span class="log-line log-header">--- 🚀 Running {script_path.name} ---</span>'
        yield full_html_output
        try:
            process = subprocess.Popen([sys.executable, str(script_path)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8', errors='replace')
            for line in iter(process.stdout.readline, ''):
                clean_line = line.strip()
                if not clean_line: continue
                # In this simple version, every line is just appended.
                # The backend should be modified to send progress as normal text.
                # For now, we just format anything with a % as a download line.
                if '%' in clean_line:
                    full_html_output += f'<span class="log-line log-download">{html.escape(clean_line)}</span>'
                else:
                    full_html_output += f'<span class="log-line">{html.escape(clean_line)}</span>'
                yield full_html_output
            process.wait()
        except Exception as e:
            full_html_output += f'<span class="log-line log-error">--- ❌ CRITICAL FAILURE: {e} ---</span>'
            yield full_html_output
            break
            
    full_html_output += '<span class="log-line log-success">--- ✅ Process Complete ---</span>'
    yield full_html_output

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
            # The UI is now extremely simple: just one HTML output.
            output_log = gr.HTML(label="Live Log", elem_id="log_output_html")

    def update_asset_choices(is_sdxl):
        models, vaes, loras, cnets = (sdxl_model_choices, sdxl_vae_choices, sdxl_lora_choices, sdxl_controlnet_choices) if is_sdxl else (sd15_model_choices, sd15_vae_choices, sd15_lora_choices, sd15_controlnet_choices)
        return [gr.update(choices=models, value=[]), gr.update(choices=vaes, value=[]), gr.update(choices=loras, value=[]), gr.update(choices=cnets, value=[])]
    
    def update_args(webui_choice): return gr.update(value=webui_selection_args.get(webui_choice, ""))
    
    sdxl_toggle.change(fn=update_asset_choices, inputs=sdxl_toggle, outputs=[model_checkboxes, vae_checkboxes, lora_checkboxes, controlnet_checkboxes])
    webui_dropdown.change(fn=update_args, inputs=webui_dropdown, outputs=args_textbox)
    
    # The launch button now has only ONE output.
    launch_button.click(
        fn=save_and_launch, 
        inputs=[webui_dropdown, sdxl_toggle, model_checkboxes, vae_checkboxes, lora_checkboxes, controlnet_checkboxes, args_textbox, ngrok_textbox, detailed_dl_checkbox], 
        outputs=[output_log]
    )

if __name__ == "__main__":
    logger.info("Self-Contained (Bulletproof) Gradio script starting...")
    ngrok_token_from_arg = sys.argv[1] if len(sys.argv) > 1 else ""
    if ngrok_token_from_arg:
        js.save(str(ANXETY_ROOT / 'settings.json'), 'WIDGETS.ngrok_token', ngrok_token_from_arg)
        logger.info("NGROK token received from command line and pre-saved.")
    
    demo.launch(share=True, inline=False)

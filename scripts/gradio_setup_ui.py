# /content/ANXETY/scripts/gradio_setup_ui.py (v5.6 - Decoupled Progress Bar Fix)

import gradio as gr
import sys
import runpy
from pathlib import Path
import subprocess
import shlex
import time
import html
import re

# --- Setup Paths & Imports ---
ANXETY_ROOT = Path('/content/ANXETY')
if str(ANXETY_ROOT) not in sys.path: sys.path.insert(0, str(ANXETY_ROOT))
from modules import json_utils as js
from modules.webui_utils import update_current_webui

# --- Data Loading ---
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
webui_selection_args = {'A1111':"--xformers --no-half-vae",'Forge':"--disable-xformers --opt-sdp-attention",'ReForge':"--xformers --cuda-stream",'Classic':"--persistent-patches --cuda-stream",'ComfyUI':"--use-sage-attention",'SD-UX':"--xformers --no-half-vae"}
MODERN_LOG_CSS="""<style>#log_output_html{background-color:#0d1117;border:1px solid #30363d;border-radius:8px;padding:12px;font-family:'Monaco','Consolas','Menlo',monospace;color:#c9d1d9;height:400px;overflow-y:auto}#log_output_html .log-line{display:block;animation:fadeIn .5s ease-in-out}#log_output_html .log-header{color:#58a6ff;font-weight:700;margin-top:15px;margin-bottom:5px;text-shadow:0 0 5px rgba(88,166,255,.3)}#log_output_html .log-success{color:#3fb950}#log_output_html .log-error{color:#f85149;font-weight:700}#log_output_html .log-download{color:#8b949e;font-size:.85em}@keyframes fadeIn{from{opacity:0;transform:translateY(5px)}to{opacity:1;transform:translateY(0)}}</style>"""

def save_and_launch(webui_choice, is_sdxl, selected_models, selected_vaes, selected_loras, selected_cnets, launch_args, ngrok_token, detailed_download):
    progress_regex = re.compile(r"\((\d{1,3})%\)")
    def format_log_line(line):
        line = html.escape(line)
        if "---" in line: return f'<span class="log-line log-header">{line}</span>'
        if "✅" in line: return f'<span class="log-line log-success">{line}</span>'
        if "❌" in line: return f'<span class="log-line log-error">{line}</span>'
        if "[#" in line and ("MiB/s" in line or "GiB/s" in line): return f'<span class="log-line log-download">{line}</span>'
        return f'<span class="log-line">{line}</span>'

    yield (format_log_line("✅ UI selections received. Saving settings..."), 0.0)
    
    settings_data = {'WIDGETS':{'change_webui':webui_choice,'sdxl_toggle':is_sdxl,'model_list':selected_models or [],'vae_list':selected_vaes or [],'lora_list':selected_loras or [],'controlnet_list':selected_cnets or [],'commandline_arguments':launch_args or "",'ngrok_token':ngrok_token or "",'detailed_download':detailed_download},'ENVIRONMENT':{'home_path':'/content'}}
    settings_path = ANXETY_ROOT / 'settings.json'
    js.save(str(settings_path), 'WIDGETS', settings_data['WIDGETS'])
    js.save(str(settings_path), 'ENVIRONMENT', settings_data['ENVIRONMENT'])
    update_current_webui(webui_choice)
    full_html_output = format_log_line("✅ Settings saved. Starting backend setup...")
    
    yield (full_html_output, 0.0)
    time.sleep(1)

    scripts_to_run = [ANXETY_ROOT/'scripts'/'en'/'downloading-en.py', ANXETY_ROOT/'scripts'/'launch.py']
    for script_path in scripts_to_run:
        full_html_output += format_log_line(f"\n--- 🚀 Running {script_path.name} ---")
        yield (full_html_output, 0.0)
        try:
            process = subprocess.Popen([sys.executable, str(script_path)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8', errors='replace')
            for line in iter(process.stdout.readline, ''):
                clean_line = line.strip()
                current_progress = 0.0
                if match := progress_regex.search(clean_line):
                    current_progress = int(match.group(1)) / 100.0
                full_html_output += format_log_line(clean_line)
                yield (full_html_output, current_progress)
            process.wait()
        except Exception as e:
             full_html_output += format_log_line(f"--- ❌ CRITICAL FAILURE: {e} ---")
             yield (full_html_output, 0.0)
             break
    full_html_output += format_log_line("\n--- ✅ Process Complete ---")
    yield (full_html_output, 0.0)

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
            # VISIBLE progress bar and INVISIBLE number for state
            download_progress = gr.Progress(label="Download Progress")
            hidden_progress_number = gr.Number(value=0, visible=False)
            
            launch_button = gr.Button("Install, Download & Launch", variant="primary")
            output_log = gr.HTML(label="Live Log", elem_id="log_output_html")

    # --- UI Interactions ---
    def update_asset_choices(is_sdxl):
        models, vaes, loras, cnets = (sdxl_model_choices, sdxl_vae_choices, sdxl_lora_choices, sdxl_controlnet_choices) if is_sdxl else (sd15_model_choices, sd15_vae_choices, sd15_lora_choices, sd15_controlnet_choices)
        return [gr.update(choices=models, value=[]), gr.update(choices=vaes, value=[]), gr.update(choices=loras, value=[]), gr.update(choices=cnets, value=[])]
    
    def update_args(webui_choice): return gr.update(value=webui_selection_args.get(webui_choice, ""))
    
    # NEW linking event handler
    def update_progress_bar(progress_value):
        return gr.update(value=progress_value, visible=True if progress_value > 0 else False)

    sdxl_toggle.change(fn=update_asset_choices, inputs=sdxl_toggle, outputs=[model_checkboxes, vae_checkboxes, lora_checkboxes, controlnet_checkboxes])
    webui_dropdown.change(fn=update_args, inputs=webui_dropdown, outputs=args_textbox)
    
    # The main launch button now outputs to the hidden number component
    launch_button.click(
        fn=save_and_launch, 
        inputs=[webui_dropdown, sdxl_toggle, model_checkboxes, vae_checkboxes, lora_checkboxes, controlnet_checkboxes, args_textbox, ngrok_textbox, detailed_dl_checkbox], 
        outputs=[output_log, hidden_progress_number] # Output to log and HIDDEN number
    )
    
    # The hidden number's change event updates the VISIBLE progress bar
    hidden_progress_number.change(
        fn=update_progress_bar,
        inputs=hidden_progress_number,
        outputs=download_progress
    )

demo.launch(share=True, inline=False)

# /content/ANXETY/scripts/gradio_setup_ui.py (v5.3 - Black Box Logging Edition)

import gradio as gr
import sys
import runpy
from pathlib import Path
import subprocess
import shlex
import time
import html
import re
import logging # Added for logging

# --- 0. Pathing (Needed before Logger) ---
try:
    ANXETY_ROOT = Path(__file__).resolve().parents[1]
except NameError:
    ANXETY_ROOT = Path('/content/ANXETY')

# --- 1. DEBUGGING LOGGER SETUP ---
LOG_DIR = ANXETY_ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "gradio_launch.log"

# Configure logging to write to both a file and the console (sys.stdout)
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s - %(asctime)s] %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, mode='w'), # 'w' to overwrite the log on each run
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)
logger.info("--- Gradio Setup UI Logger Initialized ---")

# --- 2. CSS & Imports ---
logger.debug("Defining CSS and running imports.")
MODERN_LOG_CSS = """<style>/* ... CSS content ... */</style>""" # Keep CSS as is

if str(ANXETY_ROOT) not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT))
    logger.info(f"Added '{ANXETY_ROOT}' to sys.path")

from modules import json_utils as js
from modules.webui_utils import update_current_webui
logger.info("Core modules imported.")

# --- 3. Data Loading ---
logger.info("--- Stage: Data Loading ---")
try:
    logger.debug("Loading SD1.5 data from _models-data.py...")
    sd15_data = runpy.run_path(str(ANXETY_ROOT / 'scripts/_models-data.py'))
    logger.debug("Loading SDXL data from _xl-models-data.py...")
    sdxl_data = runpy.run_path(str(ANXETY_ROOT / 'scripts/_xl-models-data.py'))
    logger.debug("Loading LoRA data from _loras-data.py...")
    loras_data_full = runpy.run_path(str(ANXETY_ROOT / 'scripts/_loras-data.py'))
    logger.info("Data files loaded via runpy.")

    # Parse data into choice lists
    sd15_model_choices = list(sd15_data.get('sd15_model_data', {}).keys())
    sd15_vae_choices = list(sd15_data.get('sd15_vae_data', {}).keys())
    sd15_controlnet_choices = list(sd15_data.get('controlnet_list', {}).keys())
    sd15_lora_choices = list(loras_data_full.get('lora_data', {}).get('sd15_loras', {}).keys())
    logger.debug(f"Created SD1.5 choices: {len(sd15_model_choices)} models, {len(sd15_lora_choices)} LoRAs.")

    sdxl_model_choices = list(sdxl_data.get('sdxl_models_data', {}).keys())
    sdxl_vae_choices = list(sdxl_data.get('sdxl_vae_data', {}).keys())
    sdxl_controlnet_choices = list(sdxl_data.get('controlnet_list', {}).keys())
    sdxl_lora_choices = list(loras_data_full.get('lora_data', {}).get('sdxl_loras', {}).keys())
    logger.debug(f"Created SDXL choices: {len(sdxl_model_choices)} models, {len(sdxl_lora_choices)} LoRAs.")
    logger.info("All asset choice lists created successfully.")

except Exception as e:
    logger.critical(f"FATAL ERROR: Could not load data files. Error: {e}", exc_info=True)
    sys.exit(1)

# ... webui_selection_args and save_and_launch function remain the same ...
webui_selection_args = {
    'A1111': "--xformers --no-half-vae --enable-insecure-extension-access --disable-console-progressbars --theme dark",
    'ComfyUI': "--use-sage-attention --dont-print-server",
    'Forge': "--disable-xformers --opt-sdp-attention --cuda-stream --pin-shared-memory --enable-insecure-extension-access --disable-console-progressbars --theme dark",
    'Classic': "--persistent-patches --cuda-stream --pin-shared-memory --enable-insecure-extension-access --disable-console-progressbars --theme dark",
    'ReForge': "--xformers --cuda-stream --pin-shared-memory --enable-insecure-extension-access --disable-console-progressbars --theme dark",
    'SD-UX': "--xformers --no-half-vae --enable-insecure-extension-access --disable-console-progressbars --theme dark"
}
def save_and_launch(webui_choice, is_sdxl, selected_models, selected_vaes, selected_loras, selected_cnets, launch_args, ngrok_token, detailed_download):
    progress_regex = re.compile(r"\((\d{1,3})%\)")
    def format_log_line(line):
        line = html.escape(line)
        if "---" in line: return f'<span class="log-line log-header">{line}</span>'
        if "✅" in line: return f'<span class="log-line log-success">{line}</span>'
        if "❌" in line: return f'<span class="log-line log-error">{line}</span>'
        if "[#" in line and ("MiB/s" in line or "GiB/s" in line): return f'<span class="log-line log-download">{line}</span>'
        return f'<span class="log-line">{line}</span>'

    yield {
        output_log: format_log_line("✅ UI selections received. Saving settings..."),
        download_progress: gr.update(value=0, visible=True)
    }
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
    yield {output_log: full_html_output, download_progress: gr.update(visible=False)}
    time.sleep(1)

    scripts_to_run = [ANXETY_ROOT/'scripts'/'en'/'downloading-en.py', ANXETY_ROOT/'scripts'/'launch.py']
    for script_path in scripts_to_run:
        full_html_output += format_log_line(f"\n--- 🚀 Running {script_path.name} ---")
        yield {output_log: full_html_output, download_progress: gr.update(value=0, visible=False)}
        try:
            process = subprocess.Popen([sys.executable, str(script_path)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8', errors='replace')
            for line in iter(process.stdout.readline, ''):
                clean_line = line.strip()
                progress_update = gr.update()
                match = progress_regex.search(clean_line)
                if match:
                    percent = int(match.group(1)) / 100.0
                    progress_update = gr.update(value=percent, visible=True)
                if "Download Results" in clean_line or "Status Legend" in clean_line:
                    progress_update = gr.update(visible=False)
                full_html_output += format_log_line(clean_line)
                yield {output_log: full_html_output, download_progress: progress_update}
            process.wait()
        except Exception as e:
             full_html_output += format_log_line(f"--- ❌ CRITICAL FAILURE: {e} ---")
             yield {output_log: full_html_output, download_progress: gr.update(visible=False)}
             break
    full_html_output += format_log_line("\n--- ✅ Process Complete ---")
    yield {output_log: full_html_output, download_progress: gr.update(visible=False)}

# --- 4. Gradio UI Definition ---
logger.info("--- Stage: UI Definition ---")
logger.debug("Entering gr.Blocks context...")
with gr.Blocks(theme=gr.themes.Soft(primary_hue="purple", secondary_hue="blue"), css=MODERN_LOG_CSS) as demo:
    logger.debug("gr.Blocks context entered. Defining UI components now.")
    gr.Markdown("# AnxietyLightning Setup")
    
    with gr.Tabs():
        with gr.TabItem("1. Setup & Asset Selection"):
            gr.Markdown("Configure your Stable Diffusion environment and select assets to download.")
            with gr.Row():
                logger.debug("Creating: webui_dropdown")
                webui_dropdown = gr.Dropdown(choices=['ReForge', 'Forge', 'A1111', 'ComfyUI', 'Classic', 'SD-UX'], value='ReForge', label="Select WebUI")
                logger.debug("Creating: sdxl_toggle")
                sdxl_toggle = gr.Checkbox(label="Use SDXL Models", value=False)
            with gr.Accordion("Asset Selection", open=True):
                with gr.Row():
                    logger.debug("Creating: model_checkboxes")
                    model_checkboxes = gr.CheckboxGroup(choices=sd15_model_choices, label="Checkpoints", interactive=True)
                    logger.debug("Creating: vae_checkboxes")
                    vae_checkboxes = gr.CheckboxGroup(choices=sd15_vae_choices, label="VAEs", interactive=True)
                with gr.Row():
                    logger.debug("Creating: lora_checkboxes")
                    lora_checkboxes = gr.CheckboxGroup(choices=sd15_lora_choices, label="LoRAs", interactive=True)
                    logger.debug("Creating: controlnet_checkboxes")
                    controlnet_checkboxes = gr.CheckboxGroup(choices=sd15_controlnet_choices, label="ControlNets", interactive=True)
            with gr.Accordion("Advanced Options", open=False):
                logger.debug("Creating: args_textbox")
                args_textbox = gr.Textbox(label="Commandline Arguments", value=webui_selection_args['ReForge'], lines=2, interactive=True)
                with gr.Row():
                    logger.debug("Creating: ngrok_textbox")
                    ngrok_textbox = gr.Textbox(label="NGROK Token", type="password", scale=3)
                    logger.debug("Creating: detailed_dl_checkbox")
                    detailed_dl_checkbox = gr.Checkbox(label="Detailed Logs", value=False, scale=1)

        with gr.TabItem("2. Launch & Live Log"):
            gr.Markdown("Click the button to begin the setup process. Progress will be displayed below.")
            logger.debug("Creating: download_progress")
            download_progress = gr.Progress()
            logger.debug("Creating: launch_button")
            launch_button = gr.Button("Install, Download & Launch", variant="primary")
            logger.debug("Creating: output_log")
            output_log = gr.HTML(label="Live Log", elem_id="log_output_html")

    logger.info("All UI components have been defined.")
    
    # --- 5. UI Interactions ---
    logger.info("--- Stage: Wiring UI Event Handlers ---")
    
    def update_asset_choices(is_sdxl):
        logger.debug(f"Executing update_asset_choices with is_sdxl={is_sdxl}")
        models = sdxl_model_choices if is_sdxl else sd15_model_choices
        vaes = sdxl_vae_choices if is_sdxl else sd15_vae_choices
        loras = sdxl_lora_choices if is_sdxl else sd15_lora_choices
        cnets = sdxl_controlnet_choices if is_sdxl else sd15_controlnet_choices
        logger.debug("Returning new choices for all asset groups.")
        return [
            gr.update(choices=models, value=[]),
            gr.update(choices=vaes, value=[]),
            gr.update(choices=loras, value=[]),
            gr.update(choices=cnets, value=[])
        ]
    
    logger.debug("Wiring event: sdxl_toggle.change")
    sdxl_toggle.change(
        fn=update_asset_choices,
        inputs=sdxl_toggle,
        outputs=[model_checkboxes, vae_checkboxes, lora_checkboxes, controlnet_checkboxes]
    )
    
    def update_args(webui_choice):
        logger.debug(f"Executing update_args with webui_choice={webui_choice}")
        return gr.update(value=webui_selection_args.get(webui_choice, ""))
        
    logger.debug("Wiring event: webui_dropdown.change")
    webui_dropdown.change(fn=update_args, inputs=webui_dropdown, outputs=args_textbox)
    
    logger.debug("Wiring event: launch_button.click")
    launch_button.click(
        fn=save_and_launch,
        inputs=[
            webui_dropdown, sdxl_toggle, model_checkboxes, vae_checkboxes,
            loras_checkboxes, controlnet_checkboxes, args_textbox, ngrok_textbox, detailed_dl_checkbox
        ],
        outputs=[output_log, download_progress]
    )

    logger.info("All event handlers wired.")

logger.info("--- Stage: Launching Gradio Demo ---")
demo.launch(share=True, inline=False)
logger.info("Gradio demo.launch() has been called.")

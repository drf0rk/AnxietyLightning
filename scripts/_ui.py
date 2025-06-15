# /scripts/_ui.py

import os
import sys
from pathlib import Path
import runpy
import gradio as gr

# --- Environment and Path Setup ---
ANXETY_ROOT = Path(os.environ.get("ANXETY_ROOT", "/content/ANXETY"))
if str(ANXETY_ROOT) not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT))

# --- Load Data and Orchestrator ---
try:
    # We load the data and the orchestrator function here, within the UI script
    sd15_data = runpy.run_path(str(ANXETY_ROOT / 'scripts/_models-data.py'))
    sdxl_data = runpy.run_path(str(ANXETY_ROOT / 'scripts/_xl-models-data.py'))
    loras_data_full = runpy.run_path(str(ANXETY_ROOT / 'scripts/_loras-data.py'))
    
    orchestrator_path = ANXETY_ROOT / 'scripts' / 'orchestrator.py'
    loaded_orchestrator = runpy.run_path(str(orchestrator_path))
    save_and_launch_generator = loaded_orchestrator['save_and_launch_generator']
    webui_selection_args = loaded_orchestrator['webui_selection_args']

    # Extract model choices for the UI
    sd15_model_choices = list(sd15_data.get('sd15_model_data', {}).keys())
    sd15_vae_choices = list(sd15_data.get('sd15_vae_data', {}).keys())
    sd15_controlnet_choices = list(sd15_data.get('controlnet_list', {}).keys())
    sd15_lora_choices = list(loras_data_full.get('lora_data', {}).get('sd15_loras', {}).keys())
    sdxl_model_choices = list(sdxl_data.get('sdxl_models_data', {}).keys())
    sdxl_vae_choices = list(sdxl_data.get('sdxl_vae_data', {}).keys())
    sdxl_controlnet_choices = list(sdxl_data.get('controlnet_list', {}).keys())
    sdxl_lora_choices = list(loras_data_full.get('lora_data', {}).get('sdxl_loras', {}).keys())
    print("✅ Asset data loaded for UI.")

except Exception as e:
    print(f"❌ FATAL [UI]: Failed to load data or orchestrator. Error: {e}")
    sys.exit(1)

# --- UI Styling ---
MODERN_LOG_CSS = \"\"\"<style>
    #log_output_html{background-color:#0d1117;border:1px solid #30363d;border-radius:8px;padding:12px;font-family:'Monaco','Consolas','Menlo',monospace;color:#c9d1d9;height:400px;overflow-y:auto}
    #log_output_html .log-line{display:block;animation:fadeIn .5s ease-in-out; white-space: pre-wrap; word-break: break-all;}
    #log_output_html .log-header{color:#58a6ff;font-weight:700;margin-top:15px;margin-bottom:5px;text-shadow:0 0 5px rgba(88,166,255,.3)}
    #log_output_html .log-success{color:#3fb950}
    #log_output_html .log-error{color:#f85149;font-weight:700}
    #log_output_html .log-warning{color:#d29922;font-weight:700}
    #log_output_html .log-url{color:#9e87ff;font-weight:700}
    #log_output_html .log-download{color:#8b949e;font-size:.85em}
    @keyframes fadeIn{from{opacity:0;transform:translateY(5px)}to{opacity:1;transform:translateY(0)}}
</style>\"\"\"

# --- Gradio UI Definition ---
with gr.Blocks(theme=gr.themes.Soft(), css=MODERN_LOG_CSS) as demo:
    gr.Markdown("## ⚡ AnxietyLightning Launcher (v29.0 - Thin Launcher Edition)")
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
                    ngrok_textbox_ui = gr.Textbox(label="NGROK Token", type="password", scale=3)
                    detailed_dl_checkbox = gr.Checkbox(label="Detailed Logs", value=False, scale=1)
        
        with gr.TabItem("2. Launch & Live Log"):
            launch_button = gr.Button("Install, Download & Launch", variant="primary")
            output_log = gr.HTML(label="Live Log", elem_id="log_output_html")

    # --- Event Handlers ---
    def update_asset_choices_local(is_sdxl):
        models, vaes, loras, cnets = (sdxl_model_choices, sdxl_vae_choices, sdxl_lora_choices, sdxl_controlnet_choices) if is_sdxl else (sd15_model_choices, sd15_vae_choices, sd15_lora_choices, sd15_controlnet_choices)
        return [gr.update(choices=models, value=[]), gr.update(choices=vaes, value=[]), gr.update(choices=loras, value=[]), gr.update(choices=cnets, value=[])]

    def update_args_local(webui_choice_val):
        return gr.update(value=webui_selection_args.get(webui_choice_val, ""))

    sdxl_toggle.change(fn=update_asset_choices_local, inputs=sdxl_toggle, outputs=[model_checkboxes, vae_checkboxes, lora_checkboxes, controlnet_checkboxes])
    webui_dropdown.change(fn=update_args_local, inputs=webui_dropdown, outputs=args_textbox)
    
    # --- Main Launch Trigger ---
    launch_button.click(
        fn=save_and_launch_generator,
        inputs=[webui_dropdown, sdxl_toggle, model_checkboxes, vae_checkboxes, lora_checkboxes, controlnet_checkboxes, args_textbox, ngrok_textbox_ui, detailed_dl_checkbox],
        outputs=[output_log]
    )

# --- Launch the UI ---
print("Launching Gradio interface...")
demo.queue().launch(share=True, inline=False, debug=True)
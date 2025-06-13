
We do not need this. We can simply define the components directly where they and render them in the correct visual sequence.

Since all the event handlers are defined *after* the `with gr.Blocks are supposed to appear in the layout. This is how Gradio is intended to be used and it will render everything in()` context, we no longer risk a `NameError`.

---

### Action: Update `gradio_setup_ui.py` with the Correct Layout

Please replace the entire content of `scripts/gradio_setup_ui.py the correct order.

### The Solution: Revert to Standard Layout Definition

We will rewrite the UI definition section to be much simpler and more direct. This will fix the upside-down layout and make the code easier to read.

**` on your GitHub with this final, corrected version. This will put everything in the right place.

```python
# /content/ANXETY/scripts/gradio_setup_ui.py (v2.1 - Correct Visual OrderAction:** Please replace the entire content of `scripts/gradio_setup_ui.py` on your GitHub with this final, corrected version.

```python
# /content/ANXETY/scripts/gradio_setup_ui.)

import gradio as gr
import sys
import runpy
from pathlib import Path
import subprocess
import shpy (v2.1 - Corrected Layout Rendering)

import gradio as gr
import sys
import runpy
from pathliblex
import time
import html

# --- 1. CSS for Modern Logging and UI Styling ---
MODERN import Path
import subprocess
import shlex
import time
import html

# --- 1. CSS for Modern_LOG_CSS = """
<style>
#log_output_html { background-color: #0d1117; border: 1px solid #30363d; border-radius:  Logging and UI Styling ---
MODERN_LOG_CSS = """
<style>
#log_output_html { background-color: #0d1117; border: 1px solid #30368px; padding: 12px; font-family: 'Monaco', 'Consolas', 'Menlo', monospace; color: #c9d1d9; height: 400px; overflow-3d; border-radius: 8px; padding: 12px; font-family: 'Monaco', 'Consolas', 'Menlo', monospace; color: #c9d1d9; height:y: auto; }
#log_output_html .log-line { display: block; animation: fadeIn 0.5s ease-in-out; }
#log_output_html .log-header { 400px; overflow-y: auto; }
#log_output_html .log-line { display: block; animation: fadeIn 0.5s ease-in-out; }
#log_ color: #58a6ff; font-weight: bold; margin-top: 15px; margin-bottom: 5px; text-shadow: 0 0 5px rgba(88,output_html .log-header { color: #58a6ff; font-weight: bold; margin-top: 15px; margin-bottom: 5px; text-shadow: 0 0 166, 255, 0.3); }
#log_output_html .log-success { color: #3fb950; }
#log_output_html .log- 5px rgba(88, 166, 255, 0.3); }
#log_output_html .log-success { color: #3fb950; }
#error { color: #f85149; font-weight: bold; }
#log_output_html .log-download { color: #8b949e; font-size: 0.log_output_html .log-error { color: #f85149; font-weight:85em; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(5px); bold; }
#log_output_html .log-download { color: #8b949e; font-size: 0.85em; }
@keyframes fadeIn { from { opacity: 0 } to { opacity: 1; transform: translateY(0); } }
</style>
"""

# --- 2. Pathing, Imports, and Data Loading ---
try:
    ANXETY_ROOT = Path(__file; transform: translateY(5px); } to { opacity: 1; transform: translateY(0); } }
</style>
"""

# --- 2. Pathing, Imports, and Data Loading ---
try:
    AN__).resolve().parents[1]
except NameError:
    ANXETY_ROOT = Path('/content/ANXETY')

if str(ANXETY_ROOT) not in sys.path:
    sys.XETY_ROOT = Path(__file__).resolve().parents[1]
except NameError:
    ANXETY_ROOT = Path('/content/ANXETY')

if str(ANXETY_ROOT) not in sys.pathpath.insert(0, str(ANXETY_ROOT))

from modules import json_utils as js
from modules.webui_utils import update_current_webui

try:
    sd15_data:
    sys.path.insert(0, str(ANXETY_ROOT))

from modules import json_utils as js
from modules.webui_utils import update_current_webui

try:
    sd1 = runpy.run_path(str(ANXETY_ROOT / 'scripts/_models-data.py'))
    sdxl_data = runpy.run_path(str(ANXETY_ROOT / '5_data = runpy.run_path(str(ANXETY_ROOT / 'scripts/_models-scripts/_xl-models-data.py'))
    loras_data_full = runpy.run_data.py'))
    sdxl_data = runpy.run_path(str(ANXETY_path(str(ANXETY_ROOT / 'scripts/_loras-data.py'))

    sd1ROOT / 'scripts/_xl-models-data.py'))
    loras_data_full = runpy.run_path(str(ANXETY_ROOT / 'scripts/_loras-data.py'))

5_model_choices = list(sd15_data.get('sd15_model_data', {}).keys())
    sd15_vae_choices = list(sd15_data.get('    sd15_model_choices = list(sd15_data.get('sd15_modelsd15_vae_data', {}).keys())
    sd15_controlnet_choices = list_data', {}).keys())
    sd15_vae_choices = list(sd15_data.get('sd15_vae_data', {}).keys())
    sd15_controlnet_(sd15_data.get('controlnet_list', {}).keys())
    sd15_lora_choices = list(loras_data_full.get('lora_data', {}).getchoices = list(sd15_data.get('controlnet_list', {}).keys())
    sd('sd15_loras', {}).keys())
    
    sdxl_model_choices = list15_lora_choices = list(loras_data_full.get('lora_data',(sdxl_data.get('sdxl_models_data', {}).keys())
    sdxl_ {}).get('sd15_loras', {}).keys())
    
    sdxl_model_vae_choices = list(sdxl_data.get('sdxl_vae_data', {}).keys())choices = list(sdxl_data.get('sdxl_models_data', {}).keys())
    
    sdxl_controlnet_choices = list(sdxl_data.get('controlnet_list',sdxl_vae_choices = list(sdxl_data.get('sdxl_vae_data', {}).keys())
    sdxl_controlnet_choices = list(sdxl_data.get('controlnet {}).keys())
    sdxl_lora_choices = list(loras_data_full.get('lora_data', {}).get('sdxl_loras', {}).keys())
except Exception as_list', {}).keys())
    sdxl_lora_choices = list(loras_data_ e:
    print(f"FATAL ERROR: Could not load data files. Error: {e}")
full.get('lora_data', {}).get('sdxl_loras', {}).keys())
    sys.exit(1)

webui_selection_args = {
    'A1111except Exception as e:
    print(f"FATAL ERROR: Could not load data files. Error: {': "--xformers --no-half-vae --enable-insecure-extension-access --disable-consolee}")
    sys.exit(1)

webui_selection_args = {
    'A1-progressbars --theme dark",
    'ComfyUI': "--use-sage-attention --dont-print111': "--xformers --no-half-vae --enable-insecure-extension-access ---server",
    'Forge': "--disable-xformers --opt-sdp-attention --cuda-stream --pin-shared-memory --enable-insecure-extension-access --disable-console-progressbars --disable-console-progressbars --theme dark",
    'ComfyUI': "--use-sage-attention --dont-print-server",
    'Forge': "--disable-xformers --opt-sdp-attention --cuda-theme dark",
    'Classic': "--persistent-patches --cuda-stream --pin-shared-memory --enablestream --pin-shared-memory --enable-insecure-extension-access --disable-console-progressbars ---insecure-extension-access --disable-console-progressbars --theme dark",
    'ReForge':theme dark",
    'Classic': "--persistent-patches --cuda-stream --pin-shared-memory --enable-insecure-extension-access --disable-console-progressbars --theme dark",
    'ReForge': "--xformers --cuda-stream --pin-shared-memory --enable-insecure-extension-access --disable-console-progressbars --theme dark",
    'SD-UX': "--xformers --no-half-vae --enable-insecure-extension-access --disable-console-progressbars --theme dark"
}

 "--xformers --cuda-stream --pin-shared-memory --enable-insecure-extension-access --disable-console-progressbars --theme dark",
    'SD-UX': "--xformers --no-half-vae --enable-insecure-extension-access --disable-console-progressbars --theme dark"
}

# --- 3. Core Logic Function ---
def save_and_launch(webui_choice, is_sdxl, selected_models, selected_vaes, selected_loras, selected_cnets, launch_# --- 3. Core Logic Function (Unchanged) ---
def save_and_launch(webui_choiceargs, ngrok_token, detailed_download):
    def format_log_line(line):
        , is_sdxl, selected_models, selected_vaes, selected_loras, selected_cnetsline = html.escape(line)
        if "---" in line: return f'<span class="log, launch_args, ngrok_token, detailed_download):
    def format_log_line(line-line log-header">{line}</span>'
        if "✅" in line: return f'<span class="log-line log-success">{line}</span>'
        if "❌" in line: return f'<):
        line = html.escape(line)
        if "---" in line: return f'<span class="log-line log-header">{line}</span>'
        if "✅" in line: return fspan class="log-line log-error">{line}</span>'
        if "[#" in line and ("Mi'<span class="log-line log-success">{line}</span>'
        if "❌" in line:B/s" in line or "GiB/s" in line): return f'<span class="log-line log-download">{line}</span>'
        return f'<span class="log-line">{line}</span> return f'<span class="log-line log-error">{line}</span>'
        if "[#" in line and ("MiB/s" in line or "GiB/s" in line): return f'<span class'

    yield format_log_line("✅ UI selections received. Saving settings...")
    settings_data =="log-line log-download">{line}</span>'
        return f'<span class="log-line">{ {
        'WIDGETS': {
            'change_webui': webui_choice, 'XL_models': is_sdxl, 'model_list': selected_models or [],
            'vae_line}</span>'

    yield format_log_line("✅ UI selections received. Saving settings...")
    settings_data = {
        'WIDGETS': {
            'change_webui': webui_list': selected_vaes or [], 'lora_list': selected_loras or [], 'controlnet_choice, 'XL_models': is_sdxl, 'model_list': selected_models or [],
            list': selected_cnets or [],
            'commandline_arguments': launch_args or "", 'ngrok'vae_list': selected_vaes or [], 'lora_list': selected_loras or [], '_token': ngrok_token or "", 'detailed_download': detailed_download
        }, 'ENVIRONMENT': {'controlnet_list': selected_cnets or [],
            'commandline_arguments': launch_args or "",home_path': '/content'}
    }
    settings_path = ANXETY_ROOT / 'settings.json'
    js.save(str(settings_path), 'WIDGETS', settings_data 'ngrok_token': ngrok_token or "", 'detailed_download': detailed_download
        }, 'ENVIRONMENT': {'home_path': '/content'}
    }
    settings_path = ANXETY_ROOT['WIDGETS'])
    js.save(str(settings_path), 'ENVIRONMENT', settings_data / 'settings.json'
    js.save(str(settings_path), 'WIDGETS',['ENVIRONMENT'])
    update_current_webui(webui_choice)
    
    full_html settings_data['WIDGETS'])
    js.save(str(settings_path), 'ENVIRONMENT', settings_data['ENVIRONMENT'])
    update_current_webui(webui_choice)
    
    _output = format_log_line("✅ Settings saved. Starting backend setup...")
    yield full_html_output
    time.sleep(1)

    scripts_to_run = [ANXETY_ROOT/'scripts'/'full_html_output = format_log_line("✅ Settings saved. Starting backend setup...")
    yield full_htmlen'/'downloading-en.py', ANXETY_ROOT/'scripts'/'launch.py']
_output
    time.sleep(1)

    scripts_to_run = [ANXETY_ROOT    for script_path in scripts_to_run:
        full_html_output += format_log_/'scripts'/'en'/'downloading-en.py', ANXETY_ROOT/'scripts'/'launchline(f"\n--- 🚀 Running {script_path.name} ---")
        yield full_html.py']
    for script_path in scripts_to_run:
        full_html_output +=_output
        try:
            process = subprocess.Popen([sys.executable, str(script_path)], format_log_line(f"\n--- 🚀 Running {script_path.name} ---")
         stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8', errors='replace')
            for line in iter(process.stdout.readline, ''):
                full_html_yield full_html_output
        try:
            process = subprocess.Popen([sys.executable, str(script_path)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utfoutput += format_log_line(line.strip())
                yield full_html_output
            process.stdout.close-8', errors='replace')
            for line in iter(process.stdout.readline, ''):
                ()
            process.wait()
            if process.returncode != 0:
                full_html_full_html_output += format_log_line(line.strip())
                yield full_html_output
            processoutput += format_log_line(f"--- ❌ ERROR: {script_path.name} exited with code {process.stdout.close()
            process.wait()
            if process.returncode != 0:
                .returncode} ---"); yield full_html_output; break
        except Exception as e:
            full_html_output += format_log_line(f"--- ❌ CRITICAL FAILURE running {script_pathfull_html_output += format_log_line(f"--- ❌ ERROR: {script_path.name} exited with code {process.returncode} ---"); yield full_html_output; break
        except Exception as e.name}: {e} ---"); yield full_html_output; break
    full_html_output += format:
            full_html_output += format_log_line(f"--- ❌ CRITICAL FAILURE running_log_line("\n--- ✅ Process Complete ---")
    yield full_html_output

# ---  {script_path.name}: {e} ---"); yield full_html_output; break
    full_html_output4. Gradio UI Definition ---
with gr.Blocks(theme=gr.themes.Soft(primary_hue="purple", secondary_hue="blue"), css=MODERN_LOG_CSS) as demo:
    gr += format_log_line("\n--- ✅ Process Complete ---")
    yield full_html_output

# --- 4. Gradio UI Definition ---
with gr.Blocks(theme=gr.themes.Soft(primary_hue="purple",.Markdown("# AnxietyLightning Setup")
    
    with gr.Tabs():
        with gr.TabItem("1. Setup secondary_hue="blue"), css=MODERN_LOG_CSS) as demo:
    gr.Markdown("# & Asset Selection"):
            gr.Markdown("Configure your Stable Diffusion environment and select assets to download.")
            
            with gr.Row():
                webui_dropdown = gr.Dropdown(choices=['ReForge', 'Forge', AnxietyLightning Setup")
    
    # Define components that will be referenced in event handlers here
    model_checkboxes = gr.CheckboxGroup(choices=sd15_model_choices, label="Checkpoints", interactive=True) 'A1111', 'ComfyUI', 'Classic', 'SD-UX'], value='ReForge', label="Select WebUI")
                sdxl_toggle = gr.Checkbox(label="Use SDXL Models
    vae_checkboxes = gr.CheckboxGroup(choices=sd15_vae_choices, label="", value=False)
            
            with gr.Accordion("Asset Selection", open=True):
                withVAEs", interactive=True)
    lora_checkboxes = gr.CheckboxGroup(choices=sd15_lora_choices, label="LoRAs", interactive=True)
    controlnet_checkboxes gr.Row():
                    model_checkboxes = gr.CheckboxGroup(choices=sd15_model_choices, label="Checkpoints", interactive=True)
                    vae_checkboxes = gr.CheckboxGroup(choices = gr.CheckboxGroup(choices=sd15_controlnet_choices, label="ControlNets", interactive=sd15_vae_choices, label="VAEs", interactive=True)
                with gr.Row=True)

    with gr.Tabs():
        with gr.TabItem("1. Setup & Asset Selection"):
():
                    lora_checkboxes = gr.CheckboxGroup(choices=sd15_lora_choices            gr.Markdown("Configure your Stable Diffusion environment and select assets to download.")
            with gr.Row():
                webui_dropdown = gr.Dropdown(choices=['ReForge', 'Forge', 'A1111, label="LoRAs", interactive=True)
                    controlnet_checkboxes = gr.CheckboxGroup(choices=sd15_controlnet_choices, label="ControlNets", interactive=True)
            
            with gr.Accordion("Advanced Options", open=False):
                args_textbox = gr.Textbox(label', 'ComfyUI', 'Classic', 'SD-UX'], value='ReForge', label="Select WebUI")
                sdxl_toggle = gr.Checkbox(label="Use SDXL Models", value=False)
="Commandline Arguments", value=webui_selection_args['ReForge'], lines=2, interactive=True)
                with gr.Row():
                    ngrok_textbox = gr.Textbox(label="NGROK            
            # We now put the variables directly into the layout. This is the fix.
            with gr.Accordion(" Token", type="password", scale=3)
                    detailed_dl_checkbox = gr.Checkbox(label="Asset Selection", open=True):
                with gr.Row():
                    model_checkboxes.render()
                    vae_Detailed Logs", value=False, scale=1)

        with gr.TabItem("2. Launch & Live Log"):
            launch_button = gr.Button("Install, Download & Launch", variant="primary")
            output_log = gr.HTML(label="Live Log", elem_id="log_output_html")

    # --- Setup ALL interactions and event handlers AFTER defining components ---
    def update_asset_choices(is_sdxl):
        models = sdxl_model_choices if is_sdxl else sd15_model_choices
        checkboxes.render()
                with gr.Row():
                    lora_checkboxes.render()
                    controlnet_checkboxes.render()
            
            with gr.Accordion("Advanced Options", open=False):
                args_textbox = gr.Textbox(label="Commandline Arguments", value=webui_selection_args['ReForge'], lines=2, interactive=True)
                with gr.Row():
                    ngrok_textbox = gr.Textbox(label="NGROK Token", type="password", scale=3)
                    detailed_dl_checkbox = gr.Checkbox(label="Detailed Logs", value=False, scale=1)

        with gr.TabItem("2. Launch & Live Log"):
            launch_button = gr.Button("Install, Download &vaes = sdxl_vae_choices if is_sdxl else sd15_vae_choices
        loras = sdxl_lora_choices if is_sdxl else sd15_lora_choices Launch", variant="primary")
            output_log = gr.HTML(label="Live Log", elem_id="log_output_html")

    # --- Setup ALL interactions and event handlers AFTER defining components ---
    def
        cnets = sdxl_controlnet_choices if is_sdxl else sd15_controlnet_choices
        return [
            gr.update(choices=models, value=[]), gr.update(choices=vaes, value=[] update_asset_choices(is_sdxl):
        models = sdxl_model_choices if is_),
            gr.update(choices=loras, value=[]), gr.update(choices=cnets, value=[])
        ]

    sdxl_toggle.change(
        fn=update_asset_choicessdxl else sd15_model_choices
        vaes = sdxl_vae_choices if is_,
        inputs=sdxl_toggle,
        outputs=[model_checkboxes, vae_checkboxessdxl else sd15_vae_choices
        loras = sdxl_lora_choices if is_sdxl else sd15_lora_choices
        cnets = sdxl_controlnet_choices if is_, lora_checkboxes, controlnet_checkboxes]
    )
    
    def update_args(webui_choice):
        return gr.update(value=webui_selection_args.get(webuisdxl else sd15_controlnet_choices
        return [
            gr.update(choices=models_choice, ""))
        
    webui_dropdown.change(fn=update_args, inputs=web, value=[]), gr.update(choices=vaes, value=[]),
            gr.update(choices=loras, value=[]), gr.update(choices=cnets, value=[])
        ]

    sdui_dropdown, outputs=args_textbox)

    launch_button.click(
        fn=save_xl_toggle.change(
        fn=update_asset_choices,
        inputs=sdxl_toggleand_launch,
        inputs=[
            webui_dropdown, sdxl_toggle, model_checkboxes,
        outputs=[model_checkboxes, vae_checkboxes, lora_checkboxes, controlnet, vae_checkboxes,
            lora_checkboxes, controlnet_checkboxes, args_textbox, ng_checkboxes]
    )
    
    def update_args(webui_choice):
        return gr.update(value=webui_selection_args.get(webui_choice, ""))
        
rok_textbox, detailed_dl_checkbox
        ],
        outputs=output_log
    )

demo.launch(share=True, inline=False)

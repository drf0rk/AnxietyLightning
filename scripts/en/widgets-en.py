# This is the new content for widgets-en.py (VERSION 7)

import ipywidgets as widgets
from IPython.display import display, clear_output
from pathlib import Path
import sys
import os
import runpy
import subprocess

# --- Configuration & Globals ---
ANXETY_ROOT = Path('/content/ANXETY')
IS_COLAB = 'google.colab' in sys.modules
VENV_PATH = Path('/content/venv')

# --- Backend Logic Helpers ---
def run_downloader(urls, output_widget):
    with output_widget:
        clear_output()
        if str(ANXETY_ROOT) not in sys.path:
            sys.path.insert(0, str(ANXETY_ROOT))
        from modules.Manager import m_download
        print(f"Starting download for {len(urls)} items...")
        for url in urls:
            if url.strip():
                m_download(url, log=True)
        print("✅ Custom file download complete.")

def run_venv_setup(output_widget):
    with output_widget:
        clear_output()
        print("--- Running VENV Downloader ---")
        # Run the downloading-en.py script to get the VENV
        get_ipython().run_line_magic('run', str(ANXETY_ROOT / 'scripts' / 'en' / 'downloading-en.py'))
        
        # Now, perform the VENV repair right here
        print("\n--- Applying VENV Patches & Fixes ---")
        VENV_BIN_PATH = VENV_PATH / 'bin'
        VENV_PYTHON_EXEC = VENV_BIN_PATH / 'python'
        CORRECT_PYTHON_PATH = f"#!/{VENV_PYTHON_EXEC.relative_to('/')}"

        if VENV_BIN_PATH.exists():
            print("  - Correcting shebang paths in venv scripts...")
            for script_path in VENV_BIN_PATH.iterdir():
                if script_path.is_file() and not script_path.is_symlink():
                    try:
                        content = script_path.read_text(encoding='utf-8', errors='ignore')
                        if content.startswith('#!/root/venv/bin/python'):
                            new_content = content.replace('#!/root/venv/bin/python', CORRECT_PYTHON_PATH, 1)
                            script_path.write_text(new_content, encoding='utf-8')
                    except Exception as e:
                        print(f"    - Could not patch {script_path.name}: {e}")
            print("  ✅ VENV shebang path correction complete.")
            
            print("  - Forcing upgrade of torch and xformers for compatibility...")
            try:
                subprocess.run([str(VENV_PYTHON_EXEC), '-m', 'pip', 'install', '--upgrade', 'torch', 'torchvision', 'torchaudio', '--index-url', 'https://download.pytorch.org/whl/cu121'], check=True, capture_output=True, text=True)
                subprocess.run([str(VENV_PYTHON_EXEC), '-m', 'pip', 'install', 'xformers'], check=True, capture_output=True, text=True)
                print("  ✅ Core libraries upgraded successfully.")
            except subprocess.CalledProcessError as e:
                print(f"  ❌ Failed to upgrade libraries: {e.stderr}")
        else:
            print("⚠️ VENV bin directory not found. Cannot apply patches.")
            
# --- UI Creation Functions ---

def create_stage2_ui(content_area):
    """Builds and displays the main asset selector UI."""
    model_data_path = ANXETY_ROOT / 'scripts/_models-data.py'
    if not model_data_path.exists():
        placeholder_ui = widgets.HTML("<h3>Error</h3><p>Could not find model data file.</p>")
        content_area.children = (placeholder_ui,)
        return

    models_data = runpy.run_path(str(model_data_path))
    model_checkboxes = [widgets.Checkbox(description=name, value=False, indent=False) for name in models_data.get('model_list', [])]
    model_widget_area = widgets.VBox(model_checkboxes)
    model_widget_area.add_class("widget-area")
    
    sdxl_toggle = widgets.ToggleButton(value=False, description='SDXL Models', button_style='info', tooltip='Toggle to show SDXL models', icon='rocket')
    
    # Placeholder for the final launch button
    launch_button = widgets.Button(description="Download Assets & Launch", icon='paper-plane', button_style='success'); launch_button.add_class("metal-button")

    model_selector_ui = widgets.VBox([widgets.HTML("<h4>Model Selector</h4>"), sdxl_toggle, model_widget_area, launch_button])
    model_selector_ui.add_class("content-container")
    
    content_area.children = (model_selector_ui,)

def create_stage1_ui():
    """Creates and displays the initial Setup UI."""
    ui_css = widgets.HTML("""<style>...</style>""") # Keeping CSS brief for clarity
    
    def detect_environment():
        if 'google.colab' in sys.modules: return "Google Colab"
        if 'KAGGLE_KERNEL_RUN_TYPE' in os.environ: return "Kaggle"
        return "Local / Unknown"
    
    PLATFORM = detect_environment()
    drive_status = "Mounted" if Path('/content/drive/MyDrive').exists() else "Not Mounted"
    venv_status = "✅ Found" if VENV_PATH.exists() else "❌ Not Found"
    header_html = widgets.HTML(f"""<div class="metal-header-container">...</div>""") # Keeping HTML brief
    
    content_area = widgets.VBox([])

    def connect_drive_click(b):
        # ... function content ...
        pass

    def open_custom_files_click(b):
        custom_urls_textarea = widgets.Textarea(placeholder='Paste one URL per line...', layout=widgets.Layout(width='99%', height='150px'))
        download_button = widgets.Button(description="Start Download", icon="download"); download_button.add_class("metal-button")
        output_widget = widgets.Output()
        
        def on_download_click(btn):
            urls = custom_urls_textarea.value.split('\n')
            run_downloader(urls, output_widget)

        download_button.on_click(on_download_click)
        downloader_ui = widgets.VBox([widgets.HTML("<h4>Extra File Downloader</h4>"), custom_urls_textarea, download_button, output_widget])
        downloader_ui.add_class("content-container")
        content_area.children = (downloader_ui,)

    def continue_to_next_stage_click(b):
        # --- NEW LOGIC ---
        # 1. Show an output area for VENV setup progress
        output_widget = widgets.Output()
        content_area.children = (output_widget,)
        
        # 2. Run VENV setup and repair, printing to the output widget
        run_venv_setup(output_widget)
        
        # 3. Once complete, build and display the Stage 2 UI
        create_stage2_ui(content_area)

    # --- Button Creation & Assembly ---
    buttons_to_display = []
    # ... button creation logic ...
    btn_continue = widgets.Button(description="Setup VENV & Continue", icon="arrow-down", tooltip="Download VENV and proceed to asset selection"); btn_continue.add_class("metal-button"); btn_continue.on_click(continue_to_next_stage_click)
    buttons_to_display.append(btn_continue)
    
    button_bar = widgets.HBox(buttons_to_display)
    centered_button_bar = widgets.Box([button_bar], layout=widgets.Layout(display='flex', justify_content='center'))
    stage1_container = widgets.VBox([ui_css, header_html, centered_button_bar, content_area])
    display(stage1_container)

# --- Main Execution ---
create_stage1_ui()

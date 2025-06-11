#
# This script represents the new, multi-stage UI logic - VERSION 6
#
# It fixes the TypeError on button clicks from the previous version.
#

import ipywidgets as widgets
from IPython.display import display, clear_output
from pathlib import Path
import sys
import os
import runpy

# --- Configuration & Environment Detection ---
ANXETY_ROOT = Path('/content/ANXETY')
IS_COLAB = 'google.colab' in sys.modules

# --- Helper function to run backend logic ---
def run_downloader(urls, output_widget):
    # This function will now write its output to the provided widget
    with output_widget:
        clear_output()
        if str(ANXETY_ROOT) not in sys.path:
            sys.path.insert(0, str(ANXETY_ROOT))
        # We need to re-import the module within the function scope for ipywidgets
        from modules.Manager import m_download

        print(f"Starting download for {len(urls)} items...")
        for url in urls:
            if url.strip():
                m_download(url, log=True)
        print("✅ Custom file download complete.")


# --- UI Creation Functions ---

def create_stage1_ui():
    """
    Creates and displays the initial Setup UI with the custom header and action buttons.
    """
    # --- 1. Custom CSS for Styling ---
    ui_css = widgets.HTML("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Roboto+Mono&display=swap');
        .metal-header-container { background: #111; border: 1px solid #333; border-radius: 8px; padding: 15px; margin-bottom: 10px; font-family: 'Roboto Mono', monospace; color: #fff; box-shadow: 0 0 15px rgba(255, 0, 0, 0.2); }
        .metal-header-title { font-family: 'Orbitron', sans-serif; font-size: 24px; font-weight: 700; color: #ff3333; text-shadow: 0 0 5px #ff0000, 0 0 10px #ff0000, 0 0 20px #ff0000; text-align: center; margin-bottom: 15px; }
        .status-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 10px; font-size: 12px; }
        .status-item { background: #222; padding: 5px 10px; border-radius: 4px; border-left: 3px solid #ff3333; }
        .status-item strong { color: #ff9999; }
        .metal-button { background-color: #222 !important; color: #ff8888 !important; border: 1px solid #ff4444 !important; font-weight: bold !important; transition: all 0.2s ease-in-out; margin: 5px; font-size: 14px !important; padding: 8px 16px !important; min-width: 150px; }
        .metal-button:hover { background-color: #ff3333 !important; color: #fff !important; box-shadow: 0 0 10px #ff3333; }
        .button-center-container { display: flex; justify-content: center; }
        .content-container { background: #1a1a1a; padding: 15px; border-radius: 6px; border: 1px solid #333; margin-top: 10px; }
        .content-container h4 { color: #ff8888; border-bottom: 1px solid #ff4444; padding-bottom: 5px; }
        .widget-area { display: flex; flex-flow: row wrap; }
        .widget-area > .widget-checkbox { flex-basis: 33%; }
    </style>
    """)

    # --- 2. Dynamic Header Content ---
    def detect_environment():
        if 'google.colab' in sys.modules: return "Google Colab"
        if 'KAGGLE_KERNEL_RUN_TYPE' in os.environ: return "Kaggle"
        return "Local / Unknown"

    PLATFORM = detect_environment()
    drive_status = "Mounted" if Path('/content/drive/MyDrive').exists() else "Not Mounted"
    venv_status = "✅ Found" if Path('/content/venv').exists() else "❌ Not Found"
    header_html = widgets.HTML(f"""
    <div class="metal-header-container">
        <div class="metal-header-title">A N X I E T Y ⚡ L I G H T N I N G</div>
        <div class="status-grid">
            <div class="status-item"><strong>PLATFORM:</strong> {PLATFORM}</div>
            <div class="status-item"><strong>ROOT:</strong> {str(ANXETY_ROOT)}</div>
            <div class="status-item"><strong>DRIVE:</strong> <span id="drive-status">{drive_status}</span></div>
            <div class="status-item"><strong>VENV:</strong> {venv_status}</div>
        </div>
    </div>
    """)

    # --- 3. Action Buttons and Dynamic Content Area ---
    content_area = widgets.VBox([])

    def connect_drive_click(b):
        if IS_COLAB:
            from google.colab import drive
            b.description = "Mounting..."; b.icon = "spinner"; b.disabled = True
            drive.mount('/content/drive')
            # This is a simple way to refresh the header - by re-creating it.
            # A more advanced JS approach is possible but more complex.
            print("✅ Google Drive Mounted at /content/drive.")
            b.description = "Drive Connected"; b.icon = "check"
        else:
            print("Drive mounting

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
def run_downloader(urls):
    if str(ANXETY_ROOT) not in sys.path:
        sys.path.insert(0, str(ANXETY_ROOT))
    from modules.Manager import m_download
    print(f"Starting download for {len(urls)} items...")
    for url in urls:
        if url.strip(): # Ensure the line is not empty
            m_download(url, log=True)
    print("✅ Custom file download complete.")


# --- UI Creation Functions ---

def create_stage1_ui():
    """
    Creates and displays the initial Setup UI with the custom header and action buttons.
    """
    # --- 1. Custom CSS for Styling ---
    header_css = widgets.HTML("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Roboto+Mono&display=swap');

        .metal-header-container {
            background: #111;
            border: 1px solid #333;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 10px;
            font-family: 'Roboto Mono', monospace;
            color: #fff;
            box-shadow: 0 0 15px rgba(255, 0, 0, 0.2);
        }
        .metal-header-title {
            font-family: 'Orbitron', sans-serif;
            font-size: 24px;
            font-weight: 700;
            color: #ff3333;
            text-shadow: 0 0 5px #ff0000, 0 0 10px #ff0000, 0 0 20px #ff0000;
            text-align: center;
            margin-bottom: 15px;
        }
        .status-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 10px;
            font-size: 12px;
        }
        .status-item {
            background: #222;
            padding: 5px 10px;
            border-radius: 4px;
            border-left: 3px solid #ff3333;
        }
        .status-item strong {
            color: #ff9999;
        }
        .metal-button {
            background-color: #222 !important;
            color: #ff8888 !important;
            border: 1px solid #ff4444 !important;
            font-weight: bold !important;
            transition: all 0.2s ease-in-out;
            margin: 5px;
            font-size: 14px !important;
            padding: 8px 16px !important;
            min-width: 150px;
        }
        .metal-button:hover {
            background-color: #ff3333 !important;
            color: #fff !important;
            box-shadow: 0 0 10px #ff3333;
        }
        .button-center-container {
            display: flex;
            justify-content: center;
        }
        .custom-downloader-container {
            background: #1a1a1a;
            padding: 15px;
            border-radius: 6px;
            border: 1px solid #333;
            margin-top: 10px;
        }
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

    # --- 3. Action Buttons and Handlers ---
    content_area = widgets.VBox([]) # This VBox will hold the dynamic content.

    def connect_drive_click(b):
        if IS_COLAB:
            from google.colab import drive
            b.description = "Mounting..."
            b.icon = "spinner"
            b.disabled = True
            drive.mount('/content/drive')
            print("✅ Google Drive Mounted at /content/drive.")
            b.description = "Drive Connected"
            b.icon = "check"
        else:
            print("Drive mounting is only available in Google Colab.")

    def open_custom_files_click(b):
        # This function now builds the real Custom Files UI
        with content_area:
            clear_output(wait=True)
            
            custom_urls_textarea = widgets.Textarea(
                placeholder='Paste one URL per line...',
                layout=widgets.Layout(width='99%', height='150px')
            )
            
            download_button = widgets.Button(description="Start Download", icon="download")
            download_button.add_class("metal-button")
            
            output_widget = widgets.Output()

            def on_download_click(btn):
                with output_widget:
                    clear_output()
                    urls = custom_urls_textarea.value.split('\\n')
                    run_downloader(urls)

            download_button.on_click(on_download_click)

            # Assemble and display the UI for this section
            downloader_ui = widgets.VBox([
                widgets.HTML("<h4>Extra File Downloader</h4>"),
                custom_urls_textarea,
                download_button,
                output_widget
            ])
            downloader_ui.add_class("custom-downloader-container")
            display(downloader_ui)

    def continue_to_main_ui_click(b):
        with content_area:
            clear_output(wait=True)
            display(widgets.HTML("<h3>Main Asset Selector (Placeholder)</h3><p>The full UI with models, LoRAs, etc., will be built here in our next step.</p>"))

    # Create and style the main action buttons
    buttons_to_display = []
    if IS_COLAB:
        btn_gdrive = widgets.Button(description="Connect Drive", icon="google-drive", tooltip="Mount Google Drive")
        btn_gdrive.add_class("metal-button")
        btn_gdrive.on_click(connect_drive_click)
        buttons_to_display.append(btn_gdrive)

    btn_custom_files = widgets.Button(description="Custom Files", icon="download", tooltip="Download extra files from URLs")
    btn_custom_files.add_class("metal-button")
    btn_custom_files.on_click(open_custom_files_click)
    buttons_to_display.append(btn_custom_files)

    btn_continue = widgets.Button(description="Continue", icon="arrow-down", tooltip="Proceed to main asset selection")
    btn_continue.add_class("metal-button")
    btn_continue.on_click(continue_to_main_ui_click)
    buttons_to_display.append(btn_continue)
    
    button_bar = widgets.HBox(buttons_to_display)
    centered_button_bar = widgets.Box([button_bar], layout=widgets.Layout(display='flex', justify_content='center'))


    # --- 4. Assemble and Display Stage 1 ---
    stage1_container = widgets.VBox([header_css, header_html, centered_button_bar, content_area])
    display(stage1_container)

# --- Main Execution ---
# When this script is run, it will start by showing the Stage 1 UI.
create_stage1_ui()

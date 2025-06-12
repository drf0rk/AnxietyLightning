# /content/ANXETY/scripts/custom_downloader.py

import ipywidgets as widgets
from IPython.display import display, clear_output
import asyncio
import ast
from pathlib import Path

# --- Self-aware pathing to allow sibling imports ---
try:
    ANXETY_ROOT = Path(__file__).resolve().parents[1]
except NameError:
    ANXETY_ROOT = Path('/content/ANXETY')

# Ensure other modules can be imported
if str(ANXETY_ROOT / 'modules') not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT / 'modules'))

from modules.widget_factory import WidgetFactory
from modules.CivitaiAPI import CivitAiAPI
import modules.json_utils as js

class CustomDownloaderUI:
    """A multi-stage UI for adding and categorizing custom model URLs."""

    def __init__(self, main_ui_launcher_callback):
        self.factory = WidgetFactory()
        self.api = CivitAiAPI(js.read(ANXETY_ROOT / 'settings.json', 'WIDGETS.civitai_token'))
        self.url_pool = []
        self.processed_data = []
        self.review_widgets = {}
        self.main_ui_launcher = main_ui_launcher_callback

        # Define layouts
        self.layout_stage1 = widgets.VBox()
        self.layout_stage2 = widgets.VBox()
        self.output_area = widgets.Output()

    def _create_stage1_ui(self):
        """Creates the UI for the initial URL input stage."""
        header = self.factory.create_header("Custom File Downloader - Stage 1: Add URLs")
        
        # URL Input
        self.url_input_text = self.factory.create_text("URL:", placeholder="Paste a Civitai or Hugging Face URL here")
        add_button = self.factory.create_button("Add to Pool", class_names=['button_save'])
        add_button.on_click(self._on_add_url_clicked)
        input_box = self.factory.create_hbox([self.url_input_text, add_button], layout={'width': '100%'})
        self.url_input_text.layout.width = '80%'

        # URL Pool Display
        pool_header = self.factory.create_html("<h4>URL Pool:</h4>")
        self.url_pool_widget = widgets.SelectMultiple(options=[], rows=10, description='', disabled=False)
        self.url_pool_widget.layout.width = '100%'
        
        # Action Buttons
        process_button = self.factory.create_button("Next: Review & Categorize", icon='arrow-right')
        process_button.on_click(self._on_process_clicked)
        skip_button = self.factory.create_button("Skip to Main Menu", icon='forward')
        skip_button.on_click(self.main_ui_launcher) # This will call the function to launch the main UI
        action_box = self.factory.create_hbox([skip_button, process_button], layout={'justify_content': 'flex-end', 'width': '100%'})

        self.layout_stage1.children = [header, input_box, pool_header, self.url_pool_widget, action_box]
        return self.layout_stage1

    def _on_add_url_clicked(self, b):
        """Callback to add a URL from the input box to the pool."""
        url = self.url_input_text.value
        if url and url not in self.url_pool:
            self.url_pool.append(url)
            self.url_pool_widget.options = self.url_pool
            self.url_input_text.value = "" # Clear input

    async def _process_and_build_stage2(self):
        """Processes URLs and builds the second stage UI."""
        self.processed_data = []
        with self.output_area:
            clear_output(wait=True)
            print("Processing URLs... This may take a moment.")
            
            for url in self.url_pool:
                if "civitai.com" in url:
                    details = self.api.get_data(url)
                    if details: self.processed_data.append(self._structure_civitai_data(details))
                elif "huggingface.co" in url:
                    self.processed_data.append(self._structure_huggingface_data(url))
        
        self._create_stage2_ui()

    def _on_process_clicked(self, b):
        """Kicks off the async processing and UI build for stage 2."""
        asyncio.ensure_future(self._process_and_build_stage2())
        
    def _structure_civitai_data(self, data):
        """Converts Civitai API response into our internal structured format."""
        return {
            "source": "Civitai",
            "name": data.get('model', {}).get('name', 'Unknown'),
            "type": data.get('model', {}).get('type', 'Unknown'),
            "base_model": data.get('baseModel', 'Unknown'),
            "files": data.get('files', []),
            "url": data.get('model', {}).get('url', '')
        }

    def _structure_huggingface_data(self, url):
        """Parses HF URL to create a guessed internal structure."""
        filename = url.split('/')[-1]
        # Basic keyword guessing
        file_type = "Checkpoint"
        if "lora" in filename.lower(): file_type = "LORA"
        if "vae" in filename.lower(): file_type = "VAE"
        
        base_model = "Unknown"
        if "sdxl" in filename.lower() or "xl" in url.lower(): base_model = "SDXL 1.0"
        elif "1.5" in filename.lower() or "1-5" in url.lower(): base_model = "SD 1.5"

        return {
            "source": "HuggingFace",
            "name": filename,
            "type": file_type,
            "base_model": base_model,
            "files": [{"name": filename, "downloadUrl": url.replace("/blob/", "/resolve/")}],
            "url": url
        }

    def _create_stage2_ui(self):
        """Creates the detailed review and categorization UI."""
        header = self.factory.create_header("Custom File Downloader - Stage 2: Review & Confirm")
        
        review_rows = []
        self.review_widgets = {} # Reset to store new widgets
        
        for i, item in enumerate(self.processed_data):
            # Create widgets for this row
            name_label = self.factory.create_html(f"<b>{item['name']}</b>")
            type_dropdown = self.factory.create_dropdown(options=['Checkpoint', 'LORA', 'VAE', 'ControlNet'], value=item['type'], description="Asset Type:")
            base_model_dropdown = self.factory.create_dropdown(options=['SD 1.5', 'SDXL 1.0', 'Pony'], value=item['base_model'], description="Base Model:")
            
            file_options = {f['name']: f['downloadUrl'] for f in item['files']}
            file_dropdown = self.factory.create_dropdown(options=list(file_options.keys()), description="File:")
            
            # Store widgets for later retrieval
            self.review_widgets[i] = {
                "type": type_dropdown,
                "base_model": base_model_dropdown,
                "file_url": file_options,
                "file_selection": file_dropdown
            }
            
            row = widgets.VBox([name_label, type_dropdown, base_model_dropdown, file_dropdown, widgets.HTML("<hr>")])
            review_rows.append(row)
            
        confirm_button = self.factory.create_button("Add to Library & Finish", icon='check', class_names=['button_save'])
        confirm_button.on_click(self._on_confirm_clicked)
        
        self.layout_stage2.children = [header, *review_rows, confirm_button]
        
        # Replace stage 1 UI with stage 2
        clear_output(wait=True)
        display(self.layout_stage2, self.output_area)
    
    def _on_confirm_clicked(self, b):
        # ... This is where the AST file writing logic would go ...
        with self.output_area:
            clear_output(wait=True)
            print("Processing complete! The new models will be available in the main UI.")
            print("NOTE: AST file writing is a complex and destructive operation. For this demo, we are skipping the actual file modification.")
            # In a real implementation, you would now call the AST writer functions.
        
        # Finally, launch the main UI
        self.main_ui_launcher(None)

    def display(self):
        """Displays the initial UI."""
        display(self._create_stage1_ui(), self.output_area)

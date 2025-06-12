# /content/ANXETY/scripts/en/widgets_en.py (v12 - Final Path Fix)

import ipywidgets as widgets
from IPython.display import display, clear_output, HTML
from pathlib import Path
import sys
import os
import runpy
import subprocess
import json
import time
from IPython import get_ipython

# --- Pathing & Imports ---
ANXETY_ROOT = Path('/content/ANXETY')
if str(ANXETY_ROOT) not in sys.path: sys.path.insert(0, str(ANXETY_ROOT))
if str(ANXETY_ROOT / 'modules') not in sys.path: sys.path.insert(0, str(ANXETY_ROOT / 'modules'))

from modules.widget_factory import WidgetFactory
from modules.webui_utils import update_current_webui, WEBUI_PATHS, DEFAULT_UI
from modules.Manager import m_clone
import modules.json_utils as js

# --- Main UI Class ---
class AnxietyUI:
    def __init__(self):
        self.factory = WidgetFactory()
        self.widgets = {}
        self.layouts = {}
        self.buttons = {}
        self.webui_selection_args = {
            'A1111': "--xformers --no-half-vae --enable-insecure-extension-access --disable-console-progressbars --theme dark",
            'ComfyUI': "--use-sage-attention --dont-print-server",
            'Forge': "--disable-xformers --opt-sdp-attention --cuda-stream --pin-shared-memory --enable-insecure-extension-access --disable-console-progressbars --theme dark",
            'Classic': "--persistent-patches --cuda-stream --pin-shared-memory --enable-insecure-extension-access --disable-console-progressbars --theme dark",
            'ReForge': "--xformers --cuda-stream --pin-shared-memory --enable-insecure-extension-access --disable-console-progressbars --theme dark",
            'SD-UX': "--xformers --no-half-vae --enable-insecure-extension-access --disable-console-progressbars --theme dark"
        }
        self.factory.load_css(ANXETY_ROOT / 'CSS' / 'main-widgets.css')

    def create_ui(self):
        self._create_widgets()
        self._create_layouts()
        self._assign_callbacks()
        self._update_model_lists()
        self._update_args_from_webui()
        display(self.layouts['main_container'])

    def _create_widgets(self):
        self.widgets['sdxl_toggle'] = self.factory.create_toggle_button(description="SDXL Models", value=False, button_style='info', tooltip='Toggle SDXL Models', icon='rocket')
        self.widgets['detailed_download'] = self.factory.create_checkbox(description="Detailed download")
        webui_options = ['ReForge', 'Forge', 'A1111', 'ComfyUI', 'Classic', 'SD-UX']
        self.widgets['change_webui'] = self.factory.create_dropdown('WebUI:', webui_options, 'ReForge')
        self.widgets['commandline_arguments'] = self.factory.create_text(description="Arguments:")
        self.widgets['model_list'], self.widgets['vae_list'], self.widgets['controlnet_list'], self.widgets['lora_list'] = [], [], [], []
        self.widgets['extension_url_input'] = self.factory.create_text("", placeholder="Paste Git Repo URL for Extension...")
        self.buttons['install_extension'] = self.factory.create_button("+", tooltip="Install this extension now")
        self.buttons['install_extension'].layout.width = '40px'
        self.widgets['embedding_url'] = self.factory.create_textarea("", placeholder="Paste Embedding URLs here, one per line...")
        self.widgets['extra_files_url'] = self.factory.create_textarea("", placeholder="Paste any other direct download URLs here...")

    def _create_layouts(self):
        self.layouts['models_box'] = widgets.VBox(self.widgets['model_list'])
        self.layouts['vaes_box'] = widgets.VBox(self.widgets['vae_list'])
        self.layouts['cnets_box'] = widgets.VBox(self.widgets['controlnet_list'])
        self.layouts['loras_box'] = widgets.VBox(self.widgets['lora_list'])
        extension_installer_box = widgets.HBox([self.widgets['extension_url_input'], self.buttons['install_extension']], layout={'width': '100%'})
        self.widgets['extension_url_input'].layout.width = '95%'
        accordion = widgets.Accordion(children=[self.layouts['models_box'], self.layouts['vaes_box'], self.layouts['cnets_box'], self.layouts['loras_box'], self.widgets['embedding_url'], extension_installer_box, self.widgets['extra_files_url']])
        titles = ['Checkpoints', 'VAEs', 'ControlNets', 'LoRAs', 'Embeddings (URL)', 'Install Extension (Git)', 'Extra Files (URL)']
        for i, title in enumerate(titles): accordion.set_title(i, title)
        self.buttons['launch'] = self.factory.create_button(description="Install, Download & Launch", class_names=['

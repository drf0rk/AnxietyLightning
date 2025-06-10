# scripts/en/widgets-en.py

import os
import sys
from pathlib import Path
import json

# Self-aware pathing to find the project root
try:
    # From .../scripts/en/ the root is 2 levels up
    ANXETY_ROOT = Path(__file__).resolve().parents[2]
except NameError:
    # Fallback for environments where __file__ is not defined
    ANXETY_ROOT = Path.cwd()

sys.path.append(str(ANXETY_ROOT))

# --- CORRECTED IMPORT ---
from modules.json_utils import save
# --- END CORRECTION ---

from modules.widget_factory import WidgetFactory
from JS.main-widgets import js_script

# Path to the JSON file where the form data will be saved
SETTINGS_PATH = ANXETY_ROOT / 'settings.json'

# Environment setup
env_data = {
    'platform': os.environ.get('COLAB_GPU', 'local'),
    'root_dir': str(ANXETY_ROOT.parent) if 'COLAB_GPU' in os.environ else str(Path.home()),
    'sd_models_shared': str(ANXETY_ROOT / 'sd_models_shared')
}
# --- CORRECTED SAVE CALL ---
save(SETTINGS_PATH, 'ENVIRONMENT', env_data)
# --- END CORRECTION ---

# UI data definition scripts
data_scripts = [
    ANXETY_ROOT / 'scripts/_models-data.py',
    ANXETY_ROOT / 'scripts/_xl-models-data.py',
    ANXETY_ROOT / 'scripts/_loras-data.py'
]

# Load data from scripts
data = {}
for script_path in data_scripts:
    with open(script_path, 'r', encoding='utf-8') as f:
        exec(f.read(), data)

factory = WidgetFactory(data)

# Create widgets
factory.create_webui_widget()
factory.create_model_widgets()
factory.create_lora_widgets()
factory.create_control_widgets()
factory.create_tool_widgets()
factory.create_download_manager_widget()
factory.create_empowerment_widget()
factory.create_season_widget()

# Display the form
factory.display_form()

# Inject JavaScript
factory.display_javascript(js_script)
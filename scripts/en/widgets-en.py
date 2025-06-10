# scripts/en/widgets-en.py

import os
import sys
from pathlib import Path

# Self-aware pathing to find the project root
try:
    # From .../scripts/en/ the root is 2 levels up
    ANXETY_ROOT = Path(__file__).resolve().parents[2]
except NameError:
    # Fallback for environments where __file__ is not defined
    ANXETY_ROOT = Path.cwd()

sys.path.append(str(ANXETY_ROOT))

from modules.json_utils import save
from modules.widget_factory import WidgetFactory

# --- START OF FIX ---
# Correctly read the JavaScript file content instead of importing it

js_file_path = ANXETY_ROOT / 'JS' / 'main-widgets.js'
try:
    with open(js_file_path, 'r', encoding='utf-8') as f:
        js_script = f.read()
except FileNotFoundError:
    print(f"ERROR: JavaScript file for widgets not found at {js_file_path}")
    # Assign an empty string to prevent the script from crashing
    js_script = ""
# --- END OF FIX ---

# Path to the JSON file where the form data will be saved
SETTINGS_PATH = ANXETY_ROOT / 'settings.json'

# Environment setup
# Determine root_dir based on the environment (Colab vs. local/other)
env_root_dir = str(ANXETY_ROOT.parent) if 'COLAB_GPU' in os.environ else str(Path.home())
env_data = {
    'platform': 'colab' if 'COLAB_GPU' in os.environ else 'local',
    'root_dir': env_root_dir,
    'sd_models_shared': str(ANXETY_ROOT / 'sd_models_shared')
}
save(SETTINGS_PATH, 'ENVIRONMENT', env_data)

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
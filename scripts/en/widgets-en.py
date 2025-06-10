# scripts/en/widgets-en.py

import os
import sys
from pathlib import Path
from ipywidgets import VBox
from IPython.display import display, HTML

# --- START OF FINAL PATHING FIX ---
# Robustly determine the project's root directory.
# The debug output shows that cwd() is likely /content, and the project is in /content/ANXETY.
cwd = Path.cwd()
project_dir_name = 'ANXETY'

if cwd.name == project_dir_name:
    ANXETY_ROOT = cwd
else:
    ANXETY_ROOT = cwd / project_dir_name

# Final check to ensure the project directory exists before proceeding.
if not ANXETY_ROOT.is_dir():
    raise FileNotFoundError(
        f"FATAL: The project root directory '{str(ANXETY_ROOT)}' was not found. "
        "This is the final check. Please ensure the repository is cloned correctly and has the name 'ANXETY'."
    )
# --- END OF FINAL PATHING FIX ---

sys.path.append(str(ANXETY_ROOT))

from modules.json_utils import save
from modules.widget_factory import WidgetFactory

# Define paths to CSS and JS files
css_file_path = ANXETY_ROOT / 'CSS' / 'main-widgets.css'
js_file_path = ANXETY_ROOT / 'JS' / 'main-widgets.js'

# Path to the JSON file where the form data will be saved
SETTINGS_PATH = ANXETY_ROOT / 'settings.json'

# Environment setup
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
    if script_path.exists():
        with open(script_path, 'r', encoding='utf-8') as f:
            exec(f.read(), data)
    else:
        print(f"Warning: Data file not found at {script_path}")

# 1. Create an instance of the factory
factory = WidgetFactory()

# 2. Create a list to hold all the widgets we want to display
ui_elements = []

# 3. Build the UI, creating and collecting widgets
ui_elements.append(factory.create_header('<h2>Environment settings</h2>'))
ui_elements.append(factory.create_dropdown(
    name='WebUI',
    options=['A1111', 'Forge', 'ReForge', 'Classic', 'ComfyUI', 'SD-UX'],
    description='Select a Stable Diffusion WebUI:'
))

ui_elements.append(factory.create_header('<h2>Models settings</h2>'))
all_models = list(data.get('models', {}).keys()) + list(data.get('xl_models', {}).keys())
ui_elements.append(factory.create_dropdown(
    name='model',
    options=all_models,
    description='Select main model:'
))
ui_elements.append(factory.create_select_multiple(
    name='additional_models',
    options=all_models,
    description='Select additional models (optional):'
))

ui_elements.append(factory.create_header('<h2>LoRAs settings</h2>'))
ui_elements.append(factory.create_select_multiple(
    name='loras',
    options=list(data.get('loras', {}).keys()),
    description='Select LoRAs:'
))

ui_elements.append(factory.create_header('<h2>Additional settings</h2>'))
ui_elements.append(factory.create_checkbox(
    name='update_webui',
    description='Update WebUI',
    value=False
))
ui_elements.append(factory.create_checkbox(
    name='update_extensions',
    description='Update Extensions',
    value=False
))
ui_elements.append(factory.create_checkbox(
    name='download_manager',
    description='Run Download Manager',
    value=True
))

ui_elements.append(factory.create_header('<h2>Empowerment mode</h2>'))
ui_elements.append(factory.create_textarea(
    name='empowerment_mode',
    placeholder='Enter download commands here...',
    description='Empowerment mode for advanced downloading:'
))

ui_elements.append(factory.create_header('<h2>Seasonal themes</h2>'))
ui_elements.append(factory.create_dropdown(
    name='season',
    options=['None', 'Christmas', 'Halloween'],
    description='Select a theme:'
))

# 4. Create a single VBox container to hold all UI elements for proper layout
form_container = VBox(ui_elements)

# 5. Load the CSS stylesheet to fix the visual layout
factory.load_css(css_file_path)

# 6. Display the container
factory.display(form_container)

# 7. Load and display the JavaScript directly
try:
    with open(js_file_path, 'r', encoding='utf-8') as f:
        js_code = f.read()
        display(HTML(f"<script>{js_code}</script>"))
except FileNotFoundError:
    print(f"ERROR: JavaScript file not found at {js_file_path}")
except Exception as e:
    print(f"An unexpected error occurred while loading JavaScript: {e}")
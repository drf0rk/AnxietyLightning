# /content/ANXETY/scripts/startup.py

# --- Imports ---
import sys
from pathlib import Path
from IPython.display import display, clear_output
from ipywidgets import HBox

# --- Pathing ---
# Ensure the project root is in the path to find other modules/scripts.
try:
    ANXETY_ROOT = Path(__file__).resolve().parents[1]
except NameError:
    ANXETY_ROOT = Path('/content/ANXETY')

if str(ANXETY_ROOT) not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT))

# --- Import from Project Modules ---
from scripts.en.widgets_en import AnxietyUI
from scripts.custom_downloader import CustomDownloaderUI
from modules.widget_factory import WidgetFactory

# --- UI State Management ---
main_ui_instance = None
downloader_ui_instance = None

# --- UI Launcher Functions ---
def launch_main_ui(b):
    """Clears output and launches the main model selection UI."""
    global main_ui_instance
    clear_output(wait=True)
    if not main_ui_instance:
        main_ui_instance = AnxietyUI()
    main_ui_instance.create_ui()

def launch_downloader_ui(b):
    """Clears output and launches the custom file downloader UI."""
    global downloader_ui_instance
    clear_output(wait=True)
    if not downloader_ui_instance:
        downloader_ui_instance = CustomDownloaderUI(launch_main_ui)
    downloader_ui_instance.display()

# --- Main Execution: Create and Display Buttons ---
if __name__ == "__main__":
    factory = WidgetFactory()
    launch_main_button = factory.create_button("Go to Main Menu", icon='rocket')
    launch_main_button.on_click(launch_main_ui)

    launch_downloader_button = factory.create_button("Open Custom Downloader", icon='download')
    launch_downloader_button.on_click(launch_downloader_ui)

    startup_box = HBox(
        [launch_main_button, launch_downloader_button],
        layout={'justify_content': 'center', 'width': '100%', 'padding': '20px'}
    )
    
    print("✓ Setup complete! Please choose an option:")
    display(startup_box)

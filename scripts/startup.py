# /content/ANXETY/scripts/startup.py (v2.3 - Absolute sys.path and Forced Reloads)

import sys
from pathlib import Path
import importlib
import ipywidgets as widgets # Keep ipywidgets here for HBox and Layout
from IPython.display import display, clear_output
from ipywidgets import HBox # HBox comes from ipywidgets

# --- Ensure ANXETY_ROOT and its subdirectories are in sys.path at the very beginning ---
# This is crucial for all relative imports to work correctly from the project root.
ANXETY_ROOT = Path('/content/ANXETY')

# Ensure these specific directories are at the start of sys.path
# This makes Python look here first for modules.
if str(ANXETY_ROOT / 'modules') not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT / 'modules'))
if str(ANXETY_ROOT / 'scripts') not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT / 'scripts'))
if str(ANXETY_ROOT / 'scripts' / 'en') not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT / 'scripts' / 'en'))
if str(ANXETY_ROOT) not in sys.path: # Add root as well, but lower priority than specific subfolders
    sys.path.insert(0, str(ANXETY_ROOT))


# Import necessary modules from the project AFTER sys.path adjustments
from modules.widget_factory import WidgetFactory # This import should now reliably find the module

# Define instances as global to persist them across button clicks if needed
main_ui_instance = None
gradio_manager_instance = None 

# --- Import Gradio Manager (do not run it directly here) ---
import scripts.gradio_manager as gm_module

def launch_main_ui(b=None):
    """Clears output and launches the main AnxietyUI (ipywidgets)."""
    global main_ui_instance
    clear_output(wait=True)
    
    # Force reload of widgets_en to ensure latest changes are picked up
    import scripts.en.widgets_en as widgets_en_module
    importlib.reload(widgets_en_module)
    AnxietyUI = widgets_en_module.AnxietyUI

    if not main_ui_instance:
        main_ui_instance = AnxietyUI()
    main_ui_instance.create_ui()

def launch_gradio_manager_ui(b=None):
    """Clears output and launches the Gradio Manager UI."""
    global gradio_manager_instance
    clear_output(wait=True)
    
    print("🚀 Launching Gradio Model Manager. Please wait for the public URL...")
    print("This Gradio app will run in the background. You can close this tab and return to the notebook.")
    
    # Force reload the gradio_manager module to pick up latest changes from disk
    importlib.reload(gm_module)
    
    try:
        print("Calling gm_module.demo.launch()...")
        gm_module.demo.launch(debug=True, share=True, quiet=False) # This starts the Gradio server
        print("Gradio Manager launched. Check for public URL above.")
    except Exception as e:
        print(f"❌ Error launching Gradio Manager: {e}", file=sys.stderr)
        print("Please check the `scripts/gradio_manager.py` file for errors.")


# --- Main Execution: Create and Display Buttons ---
if __name__ == "__main__":
    # Force reload widget_factory to ensure it's not a stale version or from a wrong path
    importlib.reload(sys.modules['modules.widget_factory']) # Reload the already imported module
    factory = WidgetFactory() 
    
    launch_main_button = factory.create_button("Go to Main WebUI Setup", icon='rocket')
    launch_main_button.on_click(launch_main_ui)

    launch_gradio_manager_button = factory.create_button("Open Gradio Model Manager", icon='download')
    launch_gradio_manager_button.on_click(launch_gradio_manager_ui)

    startup_box = HBox(
        [launch_main_button, launch_gradio_manager_button],
        layout=widgets.Layout(justify_content='center', flex_flow='row wrap')
    )
    
    display(startup_box)
    print("\nSelect an option above to proceed.")

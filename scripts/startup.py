# /content/ANXETY/scripts/startup.py (v2.0 - With Gradio Manager Launch Option)

import ipywidgets as widgets
from IPython.display import display, clear_output, HBox
import sys
from pathlib import Path
import importlib

# Ensure ANXETY_ROOT is correctly set for relative imports
ANXETY_ROOT = Path('/content/ANXETY')
if str(ANXETY_ROOT) not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT))
if str(ANXETY_ROOT / 'scripts' / 'en') not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT / 'scripts' / 'en'))
if str(ANXETY_ROOT / 'modules') not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT / 'modules'))

# Import necessary modules from the project
from modules.widget_factory import WidgetFactory

# Define instances as global to persist them across button clicks if needed
main_ui_instance = None
gradio_manager_instance = None # To hold the Gradio app instance if we need to manage it

# --- Import Gradio Manager (do not run it directly here) ---
# We'll import the module, and then in the launch function, we'll call its .launch() method.
# This import needs to be here so the `gradio_manager` module is available.
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
    
    # Gradio apps launch in a new process or thread typically
    # We will simply call the launch method of the Gradio Blocks instance from the module.
    # The gradio_manager.py script itself should handle `if __name__ == "__main__": demo.launch(...)`
    # So we just need to ensure the module is reloaded and its main launch point is called.
    
    # Reload the gradio_manager module to pick up latest changes
    importlib.reload(gm_module)
    
    # Call the launch method of the Gradio app defined in gradio_manager.py
    # This assumes 'demo' is the name of the gr.Blocks instance in gradio_manager.py
    # and its .launch() method is intended to be called this way.
    # The `launch` function in gradio_manager.py should be designed to be callable.
    try:
        # Assuming gradio_manager.py has a function like `run_gradio_app()` that launches it
        # Or, if it has `if __name__ == "__main__": demo.launch(...)`, just importing might start it.
        # However, for explicit control, it's better to have a dedicated function in gm_module.
        print("Calling gm_module.demo.launch()...")
        gm_module.demo.launch(debug=True, share=True, quiet=False) # This starts the Gradio server
        print("Gradio Manager launched. Check for public URL above.")
    except Exception as e:
        print(f"❌ Error launching Gradio Manager: {e}", file=sys.stderr)
        print("Please check the `scripts/gradio_manager.py` file for errors.")


# --- Main Execution: Create and Display Buttons ---
if __name__ == "__main__":
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

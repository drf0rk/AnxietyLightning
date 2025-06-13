# /content/ANXETY/scripts/gradio_setup_ui.py (v5.4 - TROJAN HORSE)
# The sole purpose of this script is to prove that the correct, updated
# file is being executed by the notebook launcher.

import gradio as gr
import sys
from pathlib import Path
import time

# This print statement will execute the moment the module is loaded.
# If we see this in the notebook output, we know importlib is working.
print("--- [DEBUG] TROJAN HORSE SCRIPT (v5.4) IS BEING PARSED BY PYTHON ---")
print(f"--- [DEBUG] Python Executable: {sys.executable}")
print(f"--- [DEBUG] Script Path: {Path(__file__).resolve()}")
print("--- [DEBUG] All imports successful. Preparing to launch simple UI. ---")

try:
    with gr.Blocks(theme=gr.themes.Soft()) as demo:
        gr.Markdown(
            """
            # ✅ SUCCESS: The v5.4 Trojan Horse Script is RUNNING!
            
            If you are seeing this interface, it means the following:
            
            1.  The notebook's `setup.py` correctly downloaded the **latest version** of this file from GitHub.
            2.  The `importlib` process successfully loaded and executed this script.
            3.  The original `NameError` was indeed in the old version of the script.
            
            **The deployment problem is solved. We can now restore the correct, full Gradio UI code.**
            """
        )

    # Launch the simple UI.
    print("--- [DEBUG] Launching the Trojan Horse Gradio UI... ---")
    demo.launch(share=True, inline=False)
    print("--- [DEBUG] Gradio demo.launch() has been called. The UI should be available at the public URL. ---")
    # Keep the script alive so the Gradio server doesn't shut down immediately
    while True:
        time.sleep(3600)

except Exception as e:
    # If even this simple script fails, this will catch the error.
    print(f"--- [DEBUG] ❌ A CRITICAL, UNEXPECTED ERROR OCCURRED: {e} ---")

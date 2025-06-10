# scripts/download-result.py

import sys
from pathlib import Path
import json

# Self-aware pathing: Find the project root by going up two parent directories
# This makes the script independent of the current working directory
# ANXETY_ROOT will be /content/ANXETY or /teamspace/studios/this_studio/ANXETY
try:
    ANXETY_ROOT = Path(__file__).resolve().parents[1]
except NameError:
    # Fallback for environments where __file__ is not defined (like some notebooks)
    ANXETY_ROOT = Path.cwd()

sys.path.append(str(ANXETY_ROOT))

from modules.json_utils import JsonUtils

SETTINGS_PATH = ANXETY_ROOT / 'settings.json'
CSS_PATH = ANXETY_ROOT / 'CSS' / 'download-result.css'
js = JsonUtils()

def load_settings(path):
    """Load settings from a JSON file."""
    try:
        # Check if the file exists before attempting to read
        if not Path(path).exists():
            print(f"ERROR: Settings file not found at {path}")
            return None
        
        env_data = js.read(path, 'ENVIRONMENT')
        widgets_data = js.read(path, 'WIDGETS')

        # Ensure that the reads were successful and returned dictionaries
        if env_data is None or widgets_data is None:
            print(f"ERROR: Failed to read required sections from {path}")
            if env_data is None:
                print("DEBUG: 'ENVIRONMENT' section is missing or empty.")
            if widgets_data is None:
                print("DEBUG: 'WIDGETS' section is missing or empty.")
            return None

        return {**env_data, **widgets_data}
    except Exception as e:
        print(f"An unexpected error occurred in load_settings: {e}")
        return None

# Load settings
settings = load_settings(SETTINGS_PATH)
if settings is None:
    print("FATAL: Could not load settings. Halting execution.")
    # Exit gracefully if settings can't be loaded.
    exit()

locals().update(settings)

html_content = ""
# Check if the dictionary with downloads exists and is not empty
if downloads:
    for model_type, models in downloads.items():
        if models:
            html_content += f'<div class="type-title">{model_type}</div>'
            html_content += '<div class="cards-container">'
            for model_name, model_data in models.items():
                html_content += f"""
                <div class="card">
                    <img src="{model_data['image_url']}" alt="{model_name}">
                    <div class="card-title">{model_name}</div>
                </div>
                """
            html_content += '</div>'

# Wrap the generated content in the main structure
if html_content:
    final_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Download Result</title>
        <link rel="stylesheet" href="{CSS_PATH}">
    </head>
    <body>
        <div class="main-container">
            {html_content}
        </div>
    </body>
    </html>
    """
else:
    final_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Download Result</title>
        <link rel="stylesheet" href="{CSS_PATH}">
    </head>
    <body>
        <div class="main-container">
            <div class="type-title">No assets were selected for download.</div>
        </div>
    </body>
    </html>
    """

# Print the final HTML to be captured by the notebook
print(final_html)
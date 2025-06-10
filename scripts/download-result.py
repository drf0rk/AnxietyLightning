# scripts/download-result.py

import sys
from pathlib import Path
import json

# Self-aware pathing
try:
    # From .../scripts/ the root is 1 level up
    ANXETY_ROOT = Path(__file__).resolve().parent
except NameError:
    ANXETY_ROOT = Path.cwd()

sys.path.append(str(ANXETY_ROOT))

# --- CORRECTED IMPORT ---
from modules.json_utils import read
# --- END CORRECTION ---

SETTINGS_PATH = ANXETY_ROOT / 'settings.json'
CSS_PATH = ANXETY_ROOT / 'CSS' / 'download-result.css'

def load_settings(path):
    """Load settings from a JSON file."""
    try:
        if not Path(path).exists():
            print(f"ERROR: Settings file not found at {path}")
            return None
        
        # --- CORRECTED READ CALLS ---
        env_data = read(path, 'ENVIRONMENT')
        widgets_data = read(path, 'WIDGETS')
        # --- END CORRECTION ---

        if env_data is None or widgets_data is None:
            print(f"ERROR: Failed to read required sections from {path}")
            return None

        return {**env_data, **widgets_data}
    except Exception as e:
        print(f"An unexpected error occurred in load_settings: {e}")
        return None

settings = load_settings(SETTINGS_PATH)
if settings is None:
    print("FATAL: Could not load settings. Halting execution.")
    exit()

locals().update(settings)
html_content = ""
if 'downloads' in locals() and downloads:
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

if html_content:
    final_html = f"""
    <!DOCTYPE html><html><head><title>Download Result</title><link rel="stylesheet" href="{CSS_PATH}"></head>
    <body><div class="main-container">{html_content}</div></body></html>
    """
else:
    final_html = f"""
    <!DOCTYPE html><html><head><title>Download Result</title><link rel="stylesheet" href="{CSS_PATH}"></head>
    <body><div class="main-container"><div class="type-title">No assets were selected for download.</div></div></body></html>
    """
print(final_html)
# scripts/launch.py

import os
import sys
from pathlib import Path

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
from modules.webui_utils import WebUI

# --- CORRECTED READ CALL ---
settings = read(ANXETY_ROOT / 'settings.json', 'WIDGETS')
# --- END CORRECTION ---

if settings:
    webui = WebUI(settings)
    webui.launch()
else:
    print("❌ Could not load settings. Launch failed.")
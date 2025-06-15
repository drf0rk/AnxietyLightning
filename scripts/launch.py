# /content/ANXETY/scripts/launch.py

import os
import sys
from pathlib import Path
import subprocess
import json
import shlex

# Import core modules (Assuming ANXETY_ROOT is in sys.path)
try:
    from modules import json_utils as js
    from modules import logging_utils as m
    from modules.webui_utils import get_webui_launch_command, get_webui_files
except ImportError as e:
    print(f"❌ CRITICAL: Failed to import core modules. Ensure /content/ANXETY is in sys.path. Error: {e}")
    sys.exit(1)

# --- 1. Configuration and Path Setup ---
# Use environment variables if set, otherwise default to Colab paths
HOME_DIR = Path(os.environ.get("HOME_DIR", "/content"))
ANXETY_ROOT = Path(os.environ.get("ANXETY_ROOT", "/content/ANXETY"))
SETTINGS_PATH = ANXETY_ROOT / "settings.json"
VENV_DIR = HOME_DIR / "venv"
VENV_PYTHON = VENV_DIR / "bin" / "python"

# Configure logging
m.configure_logging(ANXETY_ROOT / "logs" / "launch.log")

# --- 2. Load Settings ---
m.log("info", "--- 🚀 Stage L1: Loading Launch Configuration ---")
try:
    settings = js.read(str(SETTINGS_PATH))
    WIDGETS = settings.get('WIDGETS', {})
    WEBUI_NAME = WIDGETS.get('change_webui', 'Unknown')
    CMD_ARGS = WIDGETS.get('commandline_arguments', '')
    NGROK_TOKEN = WIDGETS.get('ngrok_token', '')

    if WEBUI_NAME == 'Unknown':
        m.log("error", "FATAL: WebUI name not found in settings.json. Cannot proceed.")
        sys.exit(1)

    m.log("info", f"Target WebUI: {WEBUI_NAME}")
    m.log("info", f"Base directory: {HOME_DIR}")
    m.log("debug", f"Loaded arguments: {CMD_ARGS}")

except Exception as e:
    m.log("error", f"FATAL: Failed to read or parse {SETTINGS_PATH}. Error: {e}")
    sys.exit(1)

# --- 3. Validate and Determine WebUI Working Directory ---
# This is the core fix: Implement fallback directory logic
m.log("info", "--- 🚀 Stage L2: Determining WebUI Working Directory ---")

# Define potential locations and required launch files
EXPECTED_WEBUI_DIR = HOME_DIR / WEBUI_NAME  # e.g., /content/ReForge
FALLBACK_WEBUI_DIR = HOME_DIR             # e.g., /content
REQUIRED_FILES = get_webui_files(WEBUI_NAME) # Gets specific files like launch.py, webui.sh, or main.py

WORKING_DIR = None
m.log("info", f"Checking for required files ({', '.join(REQUIRED_FILES)}) in expected location: {EXPECTED_WEBUI_DIR}")

# Check 1: The "Happy Path" - Zip file contained a root folder
if EXPECTED_WEBUI_DIR.is_dir():
    if any((EXPECTED_WEBUI_DIR / file).exists() for file in REQUIRED_FILES):
        WORKING_DIR = EXPECTED_WEBUI_DIR
        m.log("success", f"✅ Found WebUI files in the expected directory: {WORKING_DIR}")

# Check 2: The "Fallback Path" - Zip file extracted directly to root
if WORKING_DIR is None:
    m.log("warning", f"Expected directory {EXPECTED_WEBUI_DIR} not found or missing launch files. Checking fallback location: {FALLBACK_WEBUI_DIR}")
    if any((FALLBACK_WEBUI_DIR / file).exists() for file in REQUIRED_FILES):
        WORKING_DIR = FALLBACK_WEBUI_DIR
        m.log("success", f"✅ Found WebUI files in the fallback directory: {WORKING_DIR}")
        m.log("info", "Note: This WebUI archive was extracted directly to the root. Adjusting working directory.")

# Check 3: Failure
if WORKING_DIR is None:
    m.log("error", f"FATAL ERROR: Could not locate necessary launch files ({', '.join(REQUIRED_FILES)}) in either:")
    m.log("error", f"  - {EXPECTED_WEBUI_DIR}")
    m.log("error", f"  - {FALLBACK_WEBUI_DIR}")
    m.log("error", "The WebUI installation likely failed or the archive structure is unknown. Cannot launch.")
    sys.exit(1)

# --- 4. Validate VENV ---
m.log("info", "--- 🚀 Stage L3: Validating Virtual Environment ---")
if not VENV_PYTHON.exists():
    m.log("error", f"FATAL ERROR: Python executable not found at {VENV_PYTHON}. VENV installation failed or is corrupted.")
    sys.exit(1)
m.log("success", f"✅ VENV Python validated: {VENV_PYTHON}")

# --- 5. Prepare Launch Environment ---
m.log("info", "--- 🚀 Stage L4: Preparing Launch Environment ---")

# Environment variables for the WebUI process
webui_env = os.environ.copy()
webui_env["PYTHONPATH"] = f"{WORKING_DIR}:{webui_env.get('PYTHONPATH', '')}"
webui_env["PATH"] = f"{VENV_DIR / 'bin'}:{webui_env['PATH']}"
webui_env["HF_HOME"] = str(HOME_DIR / "cache" / "huggingface")
webui_env["TF_CPP_MIN_LOG_LEVEL"] = "3" # Reduce Tensorflow noise

# Add Ngrok if provided
if NGROK_TOKEN:
    m.log("info", "Ngrok token detected. Adding --ngrok flag.")
    CMD_ARGS = f"{CMD_ARGS} --ngrok {NGROK_TOKEN}"
else:
    m.log("info", "No Ngrok token. Using --share for Gradio link.")
    if "--share" not in CMD_ARGS:
        CMD_ARGS = f"{CMD_ARGS} --share"

# Construct the final launch command
base_command = get_webui_launch_command(WEBUI_NAME)
launch_command = f"{VENV_PYTHON} {base_command} {CMD_ARGS}"

m.log("debug", f"Final launch command: {launch_command}")
m.log("debug", f"Working directory for launch: {WORKING_DIR}")

# --- 6. Launch WebUI ---
m.log("info", "--- 🚀 Stage L5: Launching WebUI ---")
try:
    m.log("info", f"Changing current directory to {WORKING_DIR}")
    # Critical: Change to the determined working directory before launching
    os.chdir(WORKING_DIR)

    m.log("success", f"=== {WEBUI_NAME} LAUNCHING NOW ===")
    # Use shlex.split for safer command parsing if not using shell=True
    # However, many WebUIs use complex shell commands, so shell=True is often necessary but less safe.
    # We'll use Popen to stream output non-blockingly.
    process = subprocess.Popen(
        shlex.split(launch_command),
        env=webui_env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding='utf-8',
        bufsize=1
    )

    # Stream output
    for line in iter(process.stdout.readline, ''):
        print(line.strip()) # Print raw output for Gradio streamer

    process.wait()
    if process.returncode != 0:
        m.log("error", f"WebUI process exited with error code {process.returncode}")

except FileNotFoundError:
    m.log("error", f"FATAL: The launch command executable was not found. Command: {launch_command}")
except subprocess.CalledProcessError as e:
    m.log("error", f"FATAL: WebUI launch failed with exit code {e.returncode}. Check logs above for errors.")
except Exception as e:
    m.log("error", f"FATAL: An unexpected error occurred during WebUI launch: {e}")

m.log("info", "--- 🚀 Launch Script Finished ---")
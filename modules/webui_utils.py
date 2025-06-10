# ~ WebUI Utils Module | by ANXETY ~ (Final Correction for 'current' key)

import json_utils as js
from pathlib import Path
import os
import sys

def _get_project_home():
    """Determines the correct project HOME based on the runtime environment."""
    if 'google.colab' in sys.modules: return Path('/content')
    if os.path.exists('/kaggle'): return Path('/kaggle/working')
    if os.environ.get('LIGHTNING_AI') or os.path.exists('/teamspace'):
        base_path = Path('/teamspace/studios/this_studio')
        return base_path if base_path.exists() else Path.home() / 'workspace'
    return Path.cwd()

# Define paths dynamically and correctly when the module is loaded
HOME = _get_project_home()
SCR_PATH = HOME / 'ANXETY'
SETTINGS_PATH = SCR_PATH / 'settings.json'
SHARED_MODEL_BASE = HOME / 'sd_models_shared'


# --- The rest of the functions will now use the correct paths ---

WEBUI_PATHS = {
    'A1111': ('Stable-diffusion', 'VAE', 'Lora', 'embeddings', 'extensions', 'ESRGAN', 'outputs'),
    'ComfyUI': ('checkpoints', 'vae', 'loras', 'embeddings', 'custom_nodes', 'upscale_models', 'output'),
    'Classic': ('Stable-diffusion', 'VAE', 'Lora', 'embeddings', 'extensions', 'ESRGAN', 'output'),
    'ReForge': ('Stable-diffusion', 'VAE', 'Lora', 'embeddings', 'extensions', 'ESRGAN', 'outputs'),
    'SD-UX': ('Stable-diffusion', 'VAE', 'Lora', 'embeddings', 'extensions', 'ESRGAN', 'outputs')
}
DEFAULT_UI = 'Forge'

def update_current_webui(current_value):
    """Update the current WebUI value and save settings."""
    # This function now simply calls _set_webui_paths, which handles all logic.
    _set_webui_paths(current_value)

def _set_webui_paths(ui):
    """Configure paths for specified UI, pointing to the shared model base."""
    selected_ui = ui if ui in WEBUI_PATHS else DEFAULT_UI
    webui_root = HOME / selected_ui
    
    models_root = SHARED_MODEL_BASE 
    models_root.mkdir(parents=True, exist_ok=True)

    is_comfy = selected_ui == 'ComfyUI'
    
    paths = WEBUI_PATHS.get(selected_ui, WEBUI_PATHS[DEFAULT_UI])
    checkpoint_subdir, vae_subdir, lora_subdir, embed_subdir, extension_subdir, upscale_subdir, output_subdir = paths

    # THE FIX: Add 'current': ui to the dictionary that gets saved.
    path_config = {
        'current': ui, # <-- THIS LINE IS THE FIX
        'webui_path': str(webui_root),
        'model_dir': str(models_root / ('checkpoints' if is_comfy else 'Stable-diffusion')),
        'vae_dir': str(models_root / 'vae'),
        'lora_dir': str(models_root / ('loras' if is_comfy else 'Lora')),
        'embed_dir': str(models_root / 'embeddings'),
        'control_dir': str(models_root / ('controlnet' if is_comfy else 'ControlNet')),
        'upscale_dir': str(models_root / ('upscale_models' if is_comfy else 'ESRGAN')),
        'adetailer_dir': str(models_root / 'adetailer'),
        'clip_dir': str(models_root / 'clip'),
        'unet_dir': str(models_root / 'unet'),
        'vision_dir': str(models_root / 'clip_vision'),
        'encoder_dir': str(models_root / ('text_encoders' if is_comfy else 'text_encoder')),
        'diffusion_dir': str(models_root / 'diffusion_models'),
        'extension_dir': str(webui_root / extension_subdir),
        'output_dir': str(webui_root / output_subdir),
        'config_dir': str(webui_root / ('user/default' if is_comfy else ''))
    }

    # Save the complete WEBUI object to settings.
    # We read the whole file and update just the WEBUI key to be safe.
    all_settings = js.read(SETTINGS_PATH, default={})
    all_settings['WEBUI'] = path_config
    with open(SETTINGS_PATH, 'w') as f:
        json.dump(all_settings, f, indent=4)


def handle_setup_timer(webui_path, timer_webui):
    """Manage timer persistence for WebUI instances."""
    timer_file = Path(webui_path) / 'static' / 'timer.txt'
    timer_file.parent.mkdir(parents=True, exist_ok=True)
    try:
        with timer_file.open('r') as f:
            timer_webui = float(f.read())
    except (FileNotFoundError, ValueError):
        pass
    with timer_file.open('w') as f:
        f.write(str(timer_webui))
    return timer_webui
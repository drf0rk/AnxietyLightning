# /content/ANXETY/modules/webui_utils.py (Final Path Correction for Subdirectories)

from . import json_utils as js
from pathlib import Path
import os
import sys
import json

def _get_project_home():
    if 'google.colab' in sys.modules: return Path('/content')
    if os.path.exists('/kaggle'): return Path('/kaggle/working')
    if os.environ.get('LIGHTNING_AI') or os.path.exists('/teamspace'):
        base_path = Path('/teamspace/studios/this_studio')
        if not base_path.exists(): base_path = Path.home() / 'workspace'
        return base_path
    return Path.cwd()

HOME = _get_project_home()
SCR_PATH = HOME / 'ANXETY'
SETTINGS_PATH = SCR_PATH / 'settings.json'
SHARED_MODEL_BASE = HOME / 'sd_models_shared'

WEBUI_PATHS = {
    'A1111': ('Stable-diffusion', 'VAE', 'Lora', 'embeddings', 'extensions', 'ESRGAN', 'outputs'),
    'ComfyUI': ('checkpoints', 'vae', 'loras', 'embeddings', 'custom_nodes', 'upscale_models', 'output'),
    'Classic': ('Stable-diffusion', 'VAE', 'Lora', 'embeddings', 'extensions', 'ESRGAN', 'output'),
    'Forge': ('Stable-diffusion', 'VAE', 'Lora', 'embeddings', 'extensions', 'ESRGAN', 'outputs'),
    'ReForge': ('stable-diffusion-webui-reforge', 'VAE', 'Lora', 'embeddings', 'extensions', 'ESRGAN', 'outputs'),
    'SD-UX': ('Stable-diffusion', 'VAE', 'Lora', 'embeddings', 'extensions', 'ESRGAN', 'outputs')
}
DEFAULT_UI = 'Forge'

def update_current_webui(current_value):
    _set_webui_paths(current_value)

def _set_webui_paths(ui):
    selected_ui = ui if ui in WEBUI_PATHS else DEFAULT_UI
    
    webui_dir_name = 'ReForge' if selected_ui == 'ReForge' else selected_ui
    webui_root = HOME / webui_dir_name

    SHARED_MODEL_BASE.mkdir(parents=True, exist_ok=True)
    is_comfy = selected_ui == 'ComfyUI'
    
    paths = WEBUI_PATHS.get(selected_ui, WEBUI_PATHS[DEFAULT_UI])
    
    # --- FIX: Define paths to the correct subdirectories within the shared base ---
    path_config = {
        'current': ui,
        'webui_path': str(webui_root),
        'model_dir': str(SHARED_MODEL_BASE / ('checkpoints' if is_comfy else 'Stable-diffusion')),
        'vae_dir': str(SHARED_MODEL_BASE / 'VAE'),
        'lora_dir': str(SHARED_MODEL_BASE / ('loras' if is_comfy else 'Lora')),
        'embed_dir': str(SHARED_MODEL_BASE / 'embeddings'),
        'control_dir': str(SHARED_MODEL_BASE / 'ControlNet'),
        'upscale_dir': str(SHARED_MODEL_BASE / ('ESRGAN')),
        'adetailer_dir': str(SHARED_MODEL_BASE / 'adetailer'),
        'clip_dir': str(SHARED_MODEL_BASE / 'clip'),
        'unet_dir': str(SHARED_MODEL_BASE / 'unet'),
        'vision_dir': str(SHARED_MODEL_BASE / 'clip_vision'),
        'encoder_dir': str(SHARED_MODEL_BASE / ('text_encoders' if is_comfy else 'text_encoder')),
        'diffusion_dir': str(SHARED_MODEL_BASE / 'diffusion_models'),
        'extension_dir': str(webui_root / paths[4]), # extensions are UI-specific
        'output_dir': str(webui_root / paths[6]),    # outputs are UI-specific
        'config_dir': str(webui_root / ('user/default' if is_comfy else ''))
    }
    # --- END FIX ---

    for key, path_str in path_config.items():
        if '_dir' in key and not any(x in key for x in ['extension', 'output', 'config']):
            Path(path_str).mkdir(parents=True, exist_ok=True)
            
    js.save(str(SETTINGS_PATH), 'WEBUI', path_config)
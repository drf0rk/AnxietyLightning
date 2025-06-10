# /content/ANXETY/modules/webui_utils.py (Final Path Correction for ReForge's Nested Structure)

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
    
    # --- FINAL FIX: Construct the nested paths that ReForge and other UIs expect inside the shared folder ---
    models_root = SHARED_MODEL_BASE / 'models'
    
    path_config = {
        'current': ui,
        'webui_path': str(webui_root),
        'model_dir': str(models_root / ('checkpoints' if is_comfy else 'Stable-diffusion')),
        'vae_dir': str(models_root / 'VAE'),
        'lora_dir': str(models_root / ('loras' if is_comfy else 'Lora')),
        'embed_dir': str(models_root / 'embeddings'),
        'control_dir': str(models_root / 'ControlNet'),
        'upscale_dir': str(models_root / 'ESRGAN'),
        'adetailer_dir': str(models_root / 'adetailer'),
        'clip_dir': str(models_root / 'clip'),
        'unet_dir': str(models_root / 'unet'),
        'vision_dir': str(models_root / 'clip_vision'),
        'encoder_dir': str(models_root / 'text_encoders'),
        'diffusion_dir': str(models_root / 'diffusion_models'),
        'extension_dir': str(webui_root / paths[4]),
        'output_dir': str(webui_root / paths[6]),
        'config_dir': str(webui_root / ('user/default' if is_comfy else ''))
    }
    # --- END FIX ---

    for key, path_str in path_config.items():
        if '_dir' in key and not any(x in key for x in ['extension', 'output', 'config']):
            Path(path_str).mkdir(parents=True, exist_ok=True)
            
    js.save(str(SETTINGS_PATH), 'WEBUI', path_config)

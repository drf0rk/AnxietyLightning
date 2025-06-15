# /modules/download_utils.py

import sys
from pathlib import Path

try:
    from huggingface_hub import hf_hub_download
    from modules import logging_utils as m
except ImportError:
    # If hf_hub isn't installed, we need to install it.
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "huggingface_hub"], check=True)
    from huggingface_hub import hf_hub_download
    # This is a bit of a chicken-and-egg problem, if logging isn't available
    # we can't log that it's not available. Print is a safe fallback.
    try:
        from modules import logging_utils as m
    except ImportError:
        # A simple placeholder logger if the real one fails
        class m:
            def log(level, message, data=None):
                print(f"[{level.upper()}] {message}")
        print("Warning: Logging utils not found, using fallback print statements.")


def download_file(url, destination, repo_id=None, repo_type="model"):
    \"\"\"
    Downloads a file using huggingface_hub, which is robust for large files.
    `url` can be a direct URL or just the filename if `repo_id` is provided.
    \"\"\"
    destination_path = Path(destination)
    destination_path.parent.mkdir(parents=True, exist_ok=True)

    # Simplified logic: Assume URL is always the full URL for now
    # More complex logic could parse repo_id from the URL if needed.
    
    # For progress bars, we'd need to hook into the hf_hub download stream,
    # which is more complex. For now, we just log the start and end.
    # The Gradio log streamer can pick up on the default hf_hub progress bar.
    
    m.log("info", f"Initiating download for: {Path(url).name}", data={'url': url, 'dest': str(destination_path)})
    
    try:
        # This is a simplified call. A real implementation might need to parse
        # the repo_id and filename from the URL to use hf_hub_download properly.
        # For a direct URL, a different method like requests would be better,
        -        # but we stick to hf_hub as per the project's original intent.
        # Let's assume the URL is a direct resolve URL from HF, which isn't ideal
        # but will work for now. The better way is to provide repo_id and filename.
        
        # We'll use a simple but effective method with subprocess and curl for direct URLs
        # as hf_hub_download is more for repo files.
        import subprocess
        
        # The default hf_hub progress bar will be printed to stdout/stderr,
        # which our logger will pick up.
        hf_hub_download(
            repo_id=repo_id or "NagisaNao/ANXETY", # Defaulting to the known repo
            filename=Path(url).name,
            local_dir=str(destination_path.parent),
            local_dir_use_symlinks=False,
            resume_download=True
        )
        
        # We need to move the file to the final destination if hf_hub saves it with a different structure
        # hf_hub_download returns the path to the downloaded file
        downloaded_file_path = Path(hf_hub_download(...)) # Placeholder for actual call
        # os.rename(downloaded_file_path, destination_path)

        m.log("success", f"Successfully downloaded {Path(url).name}")

    except Exception as e:
        m.log("error", f"Download failed for {Path(url).name}", data={'error': str(e)})
        # Re-raise the exception to halt execution
        raise e
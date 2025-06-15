# /modules/utils.py

import os
import tarfile
import zipfile
import subprocess
import sys
from pathlib import Path

def extract(archive_path, dest_path):
    \"\"\"Extracts a given archive to a destination path.\"\"\"
    archive_path = Path(archive_path)
    dest_path = Path(dest_path)
    dest_path.mkdir(parents=True, exist_ok=True)

    if archive_path.name.endswith('.tar.lz4'):
        # We need to decompress lz4 first, then untar
        decompressed_tar_path = archive_path.with_suffix('') # a/b/c.tar.lz4 -> a/b/c.tar
        print(f"Decompressing {archive_path} with lz4...")
        subprocess.run(['lz4', '-d', str(archive_path), str(decompressed_tar_path)], check=True)
        print(f"Extracting {decompressed_tar_path}...")
        with tarfile.open(decompressed_tar_path, 'r') as tar:
            tar.extractall(path=dest_path)
        safe_remove(decompressed_tar_path) # Clean up the intermediate .tar file
    elif archive_path.name.endswith('.zip'):
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(dest_path)
    elif archive_path.name.endswith('.tar'):
        with tarfile.open(archive_path, 'r') as tar:
            tar.extractall(path=dest_path)
    else:
        raise ValueError(f"Unsupported archive format for: {archive_path.name}")

def safe_remove(path):
    \"\"\"Safely removes a file or directory, ignoring errors if it doesn't exist.\"\"\"
    try:
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.remove(path)
    except OSError:
        pass

def load_data_file(path):
    \"\"\"Executes a python file and returns its global dictionary.\"\"\"
    import runpy
    return runpy.run_path(str(path))
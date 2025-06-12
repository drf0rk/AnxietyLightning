# /content/ANXETY/modules/CivitaiAPI.py (v2.0 - Enhanced with get_model)

from urllib.parse import urlparse, parse_qs, urlencode
from typing import Optional, Tuple, Dict, Any, List
from dataclasses import dataclass, field
import requests
import os
import re

@dataclass
class ModelFile:
    name: str
    id: int
    size_kb: float
    type: str
    metadata: dict
    pickle_scan_result: str
    pickle_scan_message: str
    virus_scan_result: str
    scanned_at: str
    hashes: dict
    download_url: str
    primary: bool = False

@dataclass
class ModelVersion:
    id: int
    model_id: int
    name: str
    created_at: str
    download_url: str
    trained_words: List[str]
    base_model: str
    early_access_time_frame: int
    description: Optional[str]
    files: List[ModelFile] = field(default_factory=list)
    images: list = field(default_factory=list)
    
@dataclass
class Model:
    id: int
    name: str
    description: str
    type: str
    tags: List[str]
    creator: dict
    model_versions: List[ModelVersion] = field(default_factory=list)

class CivitAiAPI:
    BASE_URL = 'https://civitai.com/api/v1'

    def __init__(self, token: str = None):
        self.token = token
        
    def _make_request(self, endpoint: str) -> Optional[Dict]:
        try:
            url = f"{self.BASE_URL}/{endpoint}"
            headers = {'Authorization': f"Bearer {self.token}"} if self.token else {}
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"API Error: {e}")
            return None

    def get_model_id_from_url(self, url: str) -> Optional[str]:
        match = re.search(r'civitai\.com/models/(\d+)', url)
        return match.group(1) if match else None

    def get_version_id_from_url(self, url: str) -> Optional[str]:
        match = re.search(r'modelVersionId=(\d+)', url)
        if match: return match.group(1)
        match = re.search(r'models/(\d+)', url)
        return match.group(1) if match else None

    def get_data(self, url: str) -> Optional[Dict]:
        """Gets data for a specific model VERSION."""
        version_id = self.get_version_id_from_url(url)
        if not version_id: return None
        return self._make_request(f"model-versions/{version_id}")

    def get_model(self, url: str) -> Optional[Model]:
        """Gets data for an entire MODEL, including all its versions."""
        model_id = self.get_model_id_from_url(url)
        if not model_id: return None
        
        data = self._make_request(f"models/{model_id}")
        if not data: return None
        
        model_versions = []
        for v_data in data.get('modelVersions', []):
            files = [ModelFile(
                name=f.get('name'), id=f.get('id'), size_kb=f.get('sizeKB'), type=f.get('type'),
                metadata=f.get('metadata', {}), pickle_scan_result=f.get('pickleScanResult'),
                pickle_scan_message=f.get('pickleScanMessage'), virus_scan_result=f.get('virusScanResult'),
                scanned_at=f.get('scannedAt'), hashes=f.get('hashes', {}), download_url=f.get('downloadUrl'),
                primary=f.get('primary', False)
            ) for f in v_data.get('files', [])]
            
            model_versions.append(ModelVersion(
                id=v_data.get('id'), model_id=data.get('id'), name=v_data.get('name'), created_at=v_data.get('createdAt'),
                download_url=v_data.get('downloadUrl'), trained_words=v_data.get('trainedWords', []),
                base_model=v_data.get('baseModel'), early_access_time_frame=v_data.get('earlyAccessTimeFrame', 0),
                description=v_data.get('description'), files=files, images=v_data.get('images', [])
            ))

        return Model(
            id=data.get('id'), name=data.get('name'), description=data.get('description'), type=data.get('type'),
            tags=data.get('tags', []), creator=data.get('creator', {}), model_versions=model_versions
        )

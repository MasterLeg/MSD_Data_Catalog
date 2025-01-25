import io
from pathlib import Path
import requests
import zipfile

from utils import create_folder

def download_source_files(input_url: str, output_path: Path):
    response: requests.Response = requests.get(input_url)
    zip_content: bytes = response.content

    unzipped_content: zipfile.ZipFile = zipfile.ZipFile(io.BytesIO(zip_content))

    create_folder(output_path)

    unzipped_content.extractall(output_path)
    print('Extrcted files on ', output_path)
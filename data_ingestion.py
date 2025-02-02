import io
from pathlib import Path
import requests
import zipfile

from utils import create_folder

def download_source_files(input_url: str, output_path: Path):

    # Create output path
    create_folder(output_path)

    print('Downloading file: ', input_url)
    response: requests.Response = requests.get(input_url)
    zip_content: bytes = response.content

    try:
        print('Extracting ZIP file')
        unzipped_content: zipfile.ZipFile = zipfile.ZipFile(io.BytesIO(zip_content))
        unzipped_content.extractall(output_path)

    except zipfile.BadZipFile:
        print('Not a ZIP file')
        output_path = output_path.parent/(output_path.name + '.bin')
        with open(output_path, 'wb') as output_file:
            output_file.write(zip_content)

    print('Saved files on ', output_path)

def scrap_metadata() -> None:
    pass
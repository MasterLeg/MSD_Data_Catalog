import io
from pathlib import Path
import os
import requests
import yaml
import zipfile


def create_folder(folder_path: Path) -> None:
    if not folder_path.exists:
        folder_path.mkdir()


def download_source_files(input_url: str, output_path: Path):
    response: requests.Response = requests.get(input_url)
    zip_content: bytes = response.content

    unzipped_content: zipfile.ZipFile = zipfile.ZipFile(io.BytesIO(zip_content))

    create_folder(output_path)

    unzipped_content.extractall(output_path)
    print('Extrcted files on ', output_path)

def load_config_file() -> dict:
    CONFIG_FILE_NAME: str = 'config.yaml'
    PROJECT_PATH: Path = Path(os.getcwd())

    config_file_path: Path = PROJECT_PATH/CONFIG_FILE_NAME
    print(config_file_path)

    with open(config_file_path) as config_file:
        return yaml.safe_load(config_file)


def main() -> None:
    config_file_content: dict = load_config_file()
    PROJECT_PATH: Path = Path(os.getcwd())
    output_file_path: str = PROJECT_PATH/'downloads'/'pokemon'
    input_url: str = 'https://www.kaggle.com/api/v1/datasets/download/noeyislearning/pokdex'
    download_source_files(input_url, output_file_path)


if __name__ =='__main__':
    main()
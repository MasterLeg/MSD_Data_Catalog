import os
from pathlib import Path
import yaml

def create_folder(folder_path: Path) -> None:
    if not folder_path.exists:
        folder_path.mkdir()

def load_config_file(CONFIG_FILE_NAME: str = 'config.yaml') -> dict:
    PROJECT_PATH: Path = Path(os.getcwd())

    config_file_path: Path = PROJECT_PATH/CONFIG_FILE_NAME
    print(config_file_path)

    with open(config_file_path) as config_file:
        return yaml.safe_load(config_file)
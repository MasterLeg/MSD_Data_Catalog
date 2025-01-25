from pathlib import Path
import os

from utils import load_config_file
from data_ingestion import download_source_files


def main() -> None:
    config_file_content: dict = load_config_file()
    PROJECT_PATH: Path = Path(os.getcwd())

    output_file_path: str = PROJECT_PATH/'downloads'/'pokemon' # TODO: Use the config file folders path
    input_url: str = 'https://www.kaggle.com/api/v1/datasets/download/noeyislearning/pokdex' # TODO: Use the config files URLs

    download_source_files(input_url, output_file_path)


if __name__ =='__main__':
    main()
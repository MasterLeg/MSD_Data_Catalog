from pathlib import Path
import os

from utils import load_config_file
from data_ingestion import download_source_files


def main() -> None:
    config_file_content: dict = load_config_file()
    PROJECT_PATH: Path = Path(os.getcwd())

    for schema_source in config_file_content['sources']:

        output_file_path: str = PROJECT_PATH/schema_source['output']['folder_name']
        input_url: str = schema_source['url']

        download_source_files(input_url, output_file_path)


if __name__ =='__main__':
    main()
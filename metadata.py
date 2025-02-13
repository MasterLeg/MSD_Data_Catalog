import duckdb
import json
from pathlib import Path
import os

from utils import load_config_file

def create_metadata_model() -> None:
    DUCKDB_FILE_PATH: str = 'downloads\\myduckdb.db'
    METADATA_DDL_FILE_PATH: str = 'data_model\\metadata.sql'

    # Create DuckDB connection
    connection = duckdb.connect(DUCKDB_FILE_PATH)

    # Gether the DDLs from file
    with open(METADATA_DDL_FILE_PATH, 'r') as metadata_file:
        metadata_file_content: str = metadata_file.read()

    connection.execute(metadata_file_content)
    connection.close()

def handle_csv(connection: duckdb.DuckDBPyConnection,
               input_file_path: Path) -> None:
    
    raw_metadata_columns: str = ''
    try:
        raw_metadata_columns: str = connection.execute(f"SELECT Columns FROM sniff_csv('{input_file_path}')")\
                                                .fetchall()[0][0]
    except duckdb.duckdb.InvalidInputException:
        print("INVALID FILE: Execute again for: ", input_file_path)
        return

    json_content: str = raw_metadata_columns.replace("\'", '\"')
    metadata_columns: dict[str, str] = json.loads(json_content)

    return


def extract_metadata() -> None:

    config_file: dict = load_config_file()
    DUCKDB_FILE_PATH: str = 'downloads\\myduckdb.db'
    PROJECT_PATH: Path = Path(os.getcwd())

    # Create DuckDB connection
    connection = duckdb.connect(DUCKDB_FILE_PATH)

    for source, values in config_file['sources'].items():
        folder_name: str = values['output']['folder_name']
        schema_name: str = values['output']['schema_name']
        print(folder_name, schema_name)

        input_folder_path: Path = PROJECT_PATH/folder_name

        for file_path in input_folder_path.iterdir():

            print(file_path.name, file_path.suffix)

            if file_path.suffix == '.csv':
                handle_csv(connection,
                           file_path)


if __name__ == '__main__':
    create_metadata_model()
    extract_metadata()
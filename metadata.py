import duckdb

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

if __name__ == '__main__':
    create_metadata_model()
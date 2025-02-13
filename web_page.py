import streamlit as st

import duckdb
import pandas as pd
import numpy as np


def launch_web_page() -> None:

    DUCKDB_FILE_PATH: str = 'downloads\\myduckdb.db'
    # Create DuckDB connection
    connection = duckdb.connect(DUCKDB_FILE_PATH)

    st.write("""
        # Web example 1
            Ejemplo de página web""")
    
    # df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
    output_file: str = r'C:\Projects\MSD_Data_Catalog\downloads\pokedex\pokemon_bw.csv'
    df = pd.DataFrame(connection.execute(f"SELECT * FROM read_csv('{output_file}')").df().dtypes)

    st.dataframe(df)
    connection.close()


if __name__ == '__main__':
    launch_web_page()
import streamlit as st

import pandas as pd
import numpy as np


def launch_web_page() -> None:
    st.write("""
        # Web example 1
            Ejemplo de página web""")
    
    df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
    st.dataframe(df)

if __name__ == '__main__':
    launch_web_page()
import pandas as pd
from typing import List

"""
Função para concatenar a lista de dataframes para um único dataframe
"""

def concatenar_lista_dataframes (dataframe_list: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(dataframe_list)

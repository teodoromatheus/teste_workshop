from typing import List

import pandas as pd


def concatenar_lista_dataframes(
    dataframe_list: List[pd.DataFrame],
) -> pd.DataFrame:
    """
    Função para concatenar a lista de dataframes para um único dataframe

    args: dataframe_list (List[pd.DataFrame]) - lista de dataframe para ser concatenado

    return: Dataframe
    """
    return pd.concat(dataframe_list)

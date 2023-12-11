import pandas as pd
import os

def load_dataframe_to_excel (df:pd.DataFrame, nome_arquivo: str, caminho_ouput:str) -> str:
    """
    Função para carregar o dataframe final como arquivo excel na pasta de output

    args:   df (pd.Dataframe) - dataframe com os dados brutos concatenados
            nome_arquivo (str) - nome para o arquivo
            caminho_output (str) - caminho/diretório para salvar o arquivo final
    """
    if not os.path.exists(caminho_ouput):
        os.makedirs(caminho_ouput)

    df.to_excel(f"{caminho_ouput}/{nome_arquivo}.xlsx", index=False)
    return print('ETL realizado com sucesso!')
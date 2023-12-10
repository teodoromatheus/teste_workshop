import os
import glob
from typing import List
import pandas as pd

"""
Função para extrair arquivos em excel e transformar em uma lista de Dataframes

args: input_path (str): caminho da pasta com os arquivos brutos

return: lista de dataframes
"""

def extract_from_excel(path: str) -> List[pd.DataFrame]:
    all_files = glob.glob(os.path.join(path,"*.xlsx"))

    data_frame_list =  []

    for file in all_files:
        data_frame_list.append(pd.read_excel(file))
    
    return data_frame_list

if __name__  == "__main__":
    data_frame_list = extract_from_excel(path="data/data_input")
    print(data_frame_list)


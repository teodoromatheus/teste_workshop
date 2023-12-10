from pipeline.extract import extract_from_excel
from pipeline.transform import concatenar_lista_dataframes
from pipeline.load import load_dataframe_to_excel

if __name__ == "__main__":
    lista_de_dataframes = extract_from_excel(path="data/data_input")
    data_frame = concatenar_lista_dataframes(lista_de_dataframes)
    load_dataframe_to_excel(df=data_frame, nome_arquivo="arquivo_final", caminho_ouput="data/data_output")

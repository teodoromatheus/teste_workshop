from pipeline.extract import extract_from_excel

lista_de_dataframes = extract_from_excel(path="data/data_input")
print(lista_de_dataframes)
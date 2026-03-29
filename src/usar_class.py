from interface.classes.csv_class import CsvProcessor

caminho = './exemplo.csv'
filtro = 'estado'
limite = 'SP'

# Recusividade
arquivo_CSV = CsvProcessor(caminho)
arquivo_CSV.carregar_csv()
print(arquivo_CSV.filtrar_por(['estado', 'preço'], ['SP', '10,50']))


# caminho_2 = './exemplo2.csv'
# filtro_2 = 'estado'
# limite_2 = 'DF'

# caminho_csv2 = CsvProcessor(caminho_2)
# caminho_csv2.carregar_csv()
# print(caminho_csv2.filtrar_por(filtro_2, limite_2))
# # print(arquivo_CSV.df)

# print('###########################################')

# coluna = 'preço'
# atributo = '10,50'

# path_3 = CsvProcessor(caminho)
# path_3.carregar_csv()
# print(path_3.filtrar_por(filtro, limite))
# print(path_3.sub_filtro(coluna, atributo))

# path_4 = CsvProcessor(caminho_2)
# path_4.carregar_csv()
# print(path_4.filtrar_por(filtro_2, limite_2))
# print(path_4.sub_filtro(coluna,atributo))
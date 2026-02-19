import pandas as pd

class CsvProcessor:
    def __init__(self, file_path: str): # toda classe precisa de um input para inicialização, propriedades
        self.file_path = file_path # Primeira instância recebendo o caminho do arquivo
        self.df = None

    def carregar_csv(self):
        self.df = pd.read_csv(self.file_path)

    def filtros(self, coluna, atributo):
        return self.df[self.df[coluna] == atributo]
        

caminho = './exemplo.csv'
filtro = 'estado'
limite = 'SP'

arquivo_CSV = CsvProcessor(caminho)
arquivo_CSV.carregar_csv()
print(arquivo_CSV.filtros(filtro,limite))
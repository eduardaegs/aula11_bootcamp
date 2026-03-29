import pandas as pd

# Quando existem funções dentro de uma classe, devemos chamá-las de MÉTODO
#__init__ é uma funçao que vai iniciar ao chamar a classe, automaticamente
#self: Todo método de instância precisa ter self como primeiro parâmetro. self.atributo armazena dados que pertencem àquele objeto específico. 
class CsvProcessor:
    def __init__(self, file_path: str): # toda classe precisa de um input para inicialização, propriedades
        self.file_path = file_path # Primeira instância recebendo o caminho do arquivo
        self.df = None
        self.df_filtrado = None

    # O self especifica que essa funçao receberá todos os parâmetros que já estão dentro da classe
    def carregar_csv(self):
        self.df = pd.read_csv(self.file_path)

    ## Ao invés e receber uma string, receber um vetor de strings[]
    def filtrar_por(self, colunas, atributos):
        if len(colunas) != len(atributos):
            raise ValueError("Não tem o mesmo número de colunas e atributos!")
        
        if len(colunas) == 0:
            return self.df
        
        coluna_atual = colunas[0]
        atributo_atual = atributos[0]

        df_filtrado = self.df[self.df[coluna_atual] == atributo_atual]

        if len(colunas) == 1:
            return df_filtrado
        else:
            return self.filtrar_por(colunas[1:], atributos[1:])


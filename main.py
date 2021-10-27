from builtins import object

import pandas as pd
from replaceCSV import replaceCSV
from capacidade import EstudoCapacidade

arquivo_de_dados = "DadosCSV.csv"
replaceCSV(arquivo_de_dados, ',', '.')

df = pd.read_csv(arquivo_de_dados, delimiter=';', index_col=0)
print(df.head())

matrizDados = [10, 20, 30]
LSE = 30
LIE = 10

objCapacidade = EstudoCapacidade(LSE, LIE, 'Position B1', matrizDados)
print(objCapacidade.media())
print(objCapacidade.desviopadrao())
print(objCapacidade.indiceCP())

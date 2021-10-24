import pandas as pd
from replaceCSV import replaceCSV


arquivo_de_dados = "DadosCSV.csv"
replaceCSV(arquivo_de_dados, ',', '.')

df = pd.read_csv(arquivo_de_dados, delimiter=';', index_col=0)
print(df.head())


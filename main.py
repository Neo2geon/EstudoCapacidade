import pandas as pd
from replaceCSV import replaceCSV
from capacidade import EstudoCapacidade

arquivo_de_dados = "DadosCSV.csv"
replaceCSV(arquivo_de_dados, ',', '.')

df = pd.read_csv(arquivo_de_dados, delimiter=';', index_col=0)
#print(df.head())

LSE = 30
LIE = 10

objCapacidade = EstudoCapacidade(LSE, LIE, 'Position B1', df.iloc[:, 1].tolist())

print("Média: " + str(objCapacidade.media()))
print("Desvio Padrão: " + str(objCapacidade.desviopadrao()))
print("Índice CP: " + str(objCapacidade.indiceCP()))



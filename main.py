import pandas as pd
from replaceCSV import replaceCSV
from capacidade import EstudoCapacidade

arquivo_de_dados = "DadosCSV.csv"
replaceCSV(arquivo_de_dados, ',', '.')

df = pd.read_csv(arquivo_de_dados, delimiter=';', index_col=0)
#print(df.head())

LSE = 1.2
LIE = 1.1

colunaDoDf = 'Position A5'

listaDeDados =  df[colunaDoDf].tolist()
objCapacidade = EstudoCapacidade(LSE, LIE, colunaDoDf, listaDeDados)

objCapacidade.grava_arquivo_relatorio_final(objCapacidade.relatorio_final())

'''
print(objCapacidade.monta_relatorio())
print("Média: " + str(objCapacidade.media()))
print("Desvio Padrão: " + str(objCapacidade.desviopadrao()))
print("Índice CP: " + str(objCapacidade.indiceCP()))
print("CPK: " + str(objCapacidade.cpk()))
'''
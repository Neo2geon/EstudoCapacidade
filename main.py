import pandas as pd
from replaceCSV import replaceCSV
from capacidade import EstudoCapacidade

arquivo_de_dados = "DadosCSV.csv"
replaceCSV(arquivo_de_dados, ',', '.')
df = pd.read_csv(arquivo_de_dados, delimiter=';', index_col=0)
LSE = float(input('Insira o Limite Superior de Especificação: '))
LIE = float(input('Insira o Limite Inferior de Especificação: '))
for a in df:
    listaDeDados = df[a].tolist()
    objCapacidade = EstudoCapacidade(LSE, LIE, a, listaDeDados)
    objCapacidade.grava_arquivo_relatorio_final(objCapacidade.relatorio_final())
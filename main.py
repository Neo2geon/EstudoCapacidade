import pandas as pd
from replaceCSV import replaceCSV
from capacidade import EstudoCapacidade


arquivo_de_dados = "DadosCSV.csv"
replaceCSV(arquivo_de_dados, ',', '.')
df = pd.read_csv(arquivo_de_dados, delimiter=';', index_col=0)

teste = True
while teste:
    LSE = 1.25
    LIE = 1
    #LSE = float(input('\nInsira o Limite Superior de Especificação: '))
    #LIE = float(input('Insira o Limite Inferior de Especificação: '))
    if LSE<=LIE:
        print("\nO LSE não pode ser menor que o LIE.")
    else:
        teste = False

for a in df:
    listaDeDados = df[a].tolist()
    objCapacidade = EstudoCapacidade(LSE, LIE, a, listaDeDados)
    objCapacidade.grava_arquivo_relatorio_final(objCapacidade.relatorio_final())
    objCapacidade.gera_histograma()
    objCapacidade.salva_histograma()


    #grafico.get_figure().savefig('./Graficos/'+a+'.png')


print("\nRelatórios gerados com sucesso. Procure-os na pasta [Os relatórios gerados estao aqui]")
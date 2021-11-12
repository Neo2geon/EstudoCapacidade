import statistics
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt

class EstudoCapacidade:
    def __init__(self, lse: float, lie: float, label_dados: str, matriz_dados: 'lista de dados'):
        self.lse = lse
        self.lie = lie
        self.label_dados = label_dados
        self.matriz_dados = matriz_dados
        self.timestamp = str(datetime.now().strftime('%d_%m_%Y %H_%M_%S'))

    def media(self):
        return statistics.mean(self.matriz_dados)

    def desviopadrao(self):
        return statistics.stdev(self.matriz_dados)

    def indiceCP(self):
        return (self.lse - self.lie) / (6 * self.desviopadrao())

    def valor1(self):
        return (self.lse - self.media()) / (3 * self.desviopadrao())

    def valor2(self):
        return (self.media() - self.lie) / (3 * self.desviopadrao())

    def cpk(self):
        return min(self.valor1(), self.valor2())

    def relatorio_final(self):
        texto_final = '***********************          ESTUDO DE CAPACIDADE          ***********************'
        texto_final += '\n'
        texto_final += '***********************              ' + self.label_dados + '               ***********************'
        texto_final += '\n\nDados:'
        index_peca = 1
        for a in self.matriz_dados:
            texto_final += '\n' + 'Peça ' + str(index_peca) + " = " + str(a)
            index_peca += 1
        texto_final += '\n\n\nEstatísticas:'
        texto_final += '\n - Média: ' + str(self.media())
        texto_final += '\n - Desvio Padrão: ' + str(self.desviopadrao())
        texto_final += '\n - Índice CP: ' + str(self.indiceCP())
        texto_final += '\n - CPK: ' + str(self.cpk())
        return texto_final

    def grava_arquivo_relatorio_final(self, texto_final: str):
        nome_arquivo = './Os relatórios gerados estao aqui/relatorio ' + self.label_dados + " - " + str(self.timestamp) + '.txt'
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(texto_final)

    def gera_histograma(self):
        plt.subplots()
        grafico = sns.histplot(self.matriz_dados, kde=True)
        plt.axvline(self.lie, 0, max(self.matriz_dados), color = 'green')
        plt.axvline(self.lse, 0, max(self.matriz_dados), color = 'green')
        plt.title(self.label_dados)

    def salva_histograma(self):
        nome_arquivo = './Graficos/' + self.label_dados + " - " + str(self.timestamp) + '.png'
        plt.savefig(nome_arquivo)
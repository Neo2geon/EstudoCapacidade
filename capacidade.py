import statistics
from datetime import datetime

class EstudoCapacidade:
    def __init__(self, lse: float, lie: float, label_dados: str, matriz_dados: 'lista de dados'):
        self.lse = lse
        self.lie = lie
        self.label_dados = label_dados
        self.matriz_dados = matriz_dados

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
        for a in self.matriz_dados:
            texto_final += '\n' + str(a)
        texto_final += '\n\n\nEstatísticas:'
        texto_final += '\n - Média: ' + str(self.media())
        texto_final += '\n - Desvio Padrão: ' + str(self.desviopadrao())
        texto_final += '\n - Índice CP: ' + str(self.indiceCP())
        texto_final += '\n - CPK: ' + str(self.cpk())
        return texto_final

    def grava_arquivo_relatorio_final(self, texto_final: str):
        nome_arquivo = 'relatorio ' + str(datetime.now().strftime('%d_%m_%Y %H_%M_%S')) + '.txt'
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(texto_final)

import statistics

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

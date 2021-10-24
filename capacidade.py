from unittest.mock import inplace
import pandas as pd
import csv


arquivo = open('DadosCSV.csv', 'r')
textoArquivo = arquivo.read()
textoTransformado = textoArquivo.replace(',', '.')
arquivoTemporario = open('apagar.csv', 'w', encoding='utf-8')
arquivoTemporario.write(textoTransformado)
arquivoTemporario.close()


df = pd.read_csv('apagar.csv', delimiter=';', index_col=0)
print(df.head())

from unittest.mock import inplace

import pandas as pd

df = pd.read_csv('DadosCSV.csv', delimiter=';', index_col=0)
df.replace([','], '.', inplace=True)
print(df.head())
#media = df['Position A5'].mean()

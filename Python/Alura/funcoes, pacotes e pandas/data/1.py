import pandas as pd
# seta o numero de linhas para poder printar o dataframe
pd.set_option('display.max_rows', 1000)
dataset = pd.read_csv(r'C:\Users\souza\OneDrive\Documentos\db.csv', sep=';')

print(dataset)

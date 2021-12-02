import pandas as pd
# seta o numero de linhas para poder printar o dataframe
pd.set_option('display.max_rows', 1000)
# pd.set_option('display.max_columns', 100)
# dataset = pd.read_csv(r'C:\Users\souza\OneDrive\Documentos\db.csv', sep=';')
dataset = pd.read_csv(
    r'/home/italo/Documentos/GitHub/heros-journey/Python/Alura/funcoes, pacotes e pandas/data/db.csv', sep=';')

# print(dataset)
# print(dataset.dtypes)
print(dataset[['Quilometragem', 'Valor']].describe())

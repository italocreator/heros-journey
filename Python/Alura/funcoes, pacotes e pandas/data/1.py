import pandas as pd
# numero maximo de linhas 1000 para ver todo dataframe
pd.set_option('display.max_rows', 1000)
dataset = pd.read_csv(r'C:\Users\souza\OneDrive\Documentos\db.csv', sep=';')

print(dataset)

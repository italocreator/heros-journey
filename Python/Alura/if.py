# 1º item da lista - Nome do veículo
# 2º item da lista - Ano de fabricação
# 3º item da lista - Veículo é zero km?

dados = [
    ['Jetta Variant', 2003, False],
    ['Passat', 1991, False],
    ['Crossfox', 1990, False],
    ['DS5', 2019, True],
    ['Aston Martin DB4', 2006, False],
    ['Palio Weekend', 2012, False],
    ['A5', 2019, True],
    ['Série 3 Cabrio', 2009, False],
    ['Dodge Jorney', 2019, False],
    ['Carens', 2011, False]
]
dados

# carros 0 km
# carros_do_ano = []
# for lista in dados:
#     if (lista[2] == True):
#         carros_do_ano.append(lista)

# Mesmo codido por meio da list comprehensions.
carros_do_ano = [lista for lista in dados if lista[2] == True]

print(carros_do_ano)

# carros semi
# carros_semi = []
# for lista in dados:
#     if (lista[2] == False):
#         carros_semi.append(lista)

# list comprehensions.
carros_semi = [lista for lista in dados if lista[2] == False]
print(carros_semi)

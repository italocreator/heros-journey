dados = [
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I']
]

# Tradicional
result = []
for lista in dados:
    for item in lista:
        result.append(item)
result

# list comprehensions
[item for lista in dados for item in lista]

# Pode parecer uma pegadinha, mas funciona neste caso específico, o operador soma quando usado em listas retorna concatenando.
result_2 = []
for lista in dados:
    result_2 += lista
print(result_2)

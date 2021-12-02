#adicionar valores e enumerar
valores = []

for v in range(5):
    valores.append(int(input(f'Digite um valor para a posição {v+1}: ')))
maximo = max(valores)
minimo = min(valores)
print('-= * 30')
print(f'Você digitou os valores: {valores}')
print(f'O maior valor que você digitou foi {(maximo)} nas posições ', end='')
for c, v in enumerate(valores):
    if v == maximo:
        print(f'{c+1}...', end='')
print(f'\nO menor valor que você digitou foi {(minimo)} nas posições ', end='')
for c, v in enumerate(valores):
    if v == minimo:
        print(f'{c+1}...', end='')

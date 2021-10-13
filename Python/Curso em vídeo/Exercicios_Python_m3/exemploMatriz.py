matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(
            input(f'Digite um valor: [{linha}, {coluna}] '))
# estrutura de repetição para alimentar a matriz
print('-=' * 30)
# estrutura para impressão dos dados em formato de matriz
for linha in range(0, 3):
    for coluna in range(0, 3):
        # :^5 centraliza as casas com 5 espaços
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()  # fazer a quebra da coluna

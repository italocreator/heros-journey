# manipulando tuplas
lista_escolar = ('lapis', 1.75,
                 'borracha', 2,
                 'estojo', 15.90,
                 'transferidor', 4.20,
                 'compasso', 9.99,
                 'mochila', 120.32,
                 'cametas', 22.30,
                 'livro', 34.90)
print('-' * 30)
print('LISTAGEM DE PREÇOS')
print('-' * 30)
for pos in range(0, len(lista_escolar)):
    if pos % 2 == 0:
        print(f'{lista_escolar[pos]:.<30}', end='')
    else:
        print(f'R${lista_escolar[pos]:>7.2f}')

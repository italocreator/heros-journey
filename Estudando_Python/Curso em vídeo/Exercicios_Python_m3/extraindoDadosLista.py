numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'nN':
        break
print(f'Você digitou {len(numeros)} elementos.')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {numeros}')
if 5 in numeros:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')

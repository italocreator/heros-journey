# '''Exercício Python 084: Faça um programa que leia nome e Peso de várias pessoas,
# Guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.'''

pessoapeso = []
galera = []
maiorpeso = 0
menorpeso = 0
contadorpessoas = 0

while True:
    pessoapeso.append(str(input('Nome: ')))
    pessoapeso.append(float(input('Peso: ')))
    if len(galera) == 0:
        maiorpeso = menorpeso = pessoapeso[1]
    else:
        if pessoapeso[1] > maiorpeso:
            maiorpeso = pessoapeso[1]
        if pessoapeso[1] < menorpeso:
            menorpeso = pessoapeso[1]

    galera.append(pessoapeso[:])
    pessoapeso.clear()
    resposta = str(input('Quer continuar? [S/N/] '))
    contadorpessoas += 1
    if resposta in 'nN':
        break
print(f'Total de pessoas cadastradas: {contadorpessoas}')
print(f'O maior peso foi de {maiorpeso}Kg. Peso de ', end='')
for p in galera:
    if p[1] == maiorpeso:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menorpeso}Kg. Peso de ', end='')
for p in galera:
    if p[1] == menorpeso:
        print(f'[{p[0]}]', end='')

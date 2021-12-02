# '''Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

numeros = []
pares = []
impares = []

while True:
    numeros.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N/] '))
    if resposta in "nN":
        break
for i, v in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
numeros.sort()
print('-=' * 45)
print(f'A lista completa em ordem crescente é: {numeros}')
print(f'O numeros pares foram: {pares}')
print(f'E os numeros impares foram: {impares}')

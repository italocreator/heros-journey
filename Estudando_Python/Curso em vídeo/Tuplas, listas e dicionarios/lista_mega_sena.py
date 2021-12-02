# '''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import randint
lista = list()
jogos = list()
print('-=' * 30)
print('                      MEGA SENA                          ')
print('-=' * 30)
contador = 0
numero_de_jogos = int(input('Quantos jogos você quer? '))
total = 0

while total <= numero_de_jogos:
    contador = 0
    while True:
        numeros = randint(1, 60)
        if numeros not in lista:
            lista.append(numeros)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-='*3, f'SORTEANDO {numero_de_jogos} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i}: {l}')

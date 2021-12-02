# adivinhe o numero
from random import randint
from time import sleep

computador = randint(0, 5)  # algoritimo escolhe numero aleatorio de 0 a 5
print('-=-' * 20)
print('Pensarei em um número de 0 a 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Digite um numero de 0 a 5: '))
print('Pensando...')
sleep(1.5)
if jogador == computador:
    print('Que bruxaria é essa? como você acertou?!')
else:
    print('HahHAhahah! errou, pensei no numero {}'.format(computador))

from time import sleep
from random import randint
print('Sou seu computador...')
sleep(0.5)
print('Acabei de pensar em um número entre 0 e 10.')
sleep(0.5)
print('Será que você consegue adivinhar ?')
sleep(0.5)
tentativas = 0
cpnum = randint(0, 10)
acertou = False
while not acertou:
    num = int(input('Qual é o seu palpite? '))
    tentativas += 1
    if num == cpnum:
        acertou = True
    else:
        if num > cpnum:
            print('Menos... tente mais uma vez... ')
        elif num < cpnum:
            print('Mais... tente mais uma vez... ')
print('Acertou com {} tentativas. Parabéns!'.format(tentativas))

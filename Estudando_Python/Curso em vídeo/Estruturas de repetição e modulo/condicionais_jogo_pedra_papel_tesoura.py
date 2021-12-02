from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
player2 = randint(0, 2)
print('O Player 2 escolheu {}'.format(itens[player2]))
print(
    '''Escolha uma opção:
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA
    '''
)
player1 = int(input('Qual a sua escolha? '))
while player1 > 2:
    player1 = int(input('\033[31mJogada INVALIDA, tente novamente:\033[m '))
print('\033[32mJO\033[m')
sleep(1)
print('\033[33mKEN\033m')
sleep(1)
print('\033[31mPO\033[m')
sleep(1)
print('\033[33m-=\033[m' * 20)
print('Você escolheu: {}'.format(itens[player1]))
print('O Player 2 escolheu: {}'.format(itens[player2]))
print('\033[33m-=\033[m' * 20)
if player1 == 0:
    if player2 == 0:
        print('EMPATE!')
    elif player2 == 1:
        print('\033[31mVocê PERDEU!\033[m')
    elif player2 == 2:
        print('\033[32mVocê Ganhou!\033[m')
    else:
        print('Jogada invalida')
if player1 == 1:
    if player2 == 0:
        print('\033[32mVocê Ganhou!\033[m')
    elif player2 == 1:
        print('EMPATE!')
    elif player2 == 2:
        print('\033[31mVocê PERDEU!\033[m')
    else:
        print('Jogada invalida')
if player1 == 2:
    if player2 == 0:
        print('\033[31mVocê PERDEU!\033[m')
    elif player2 == 1:
        print('\033[32mVocê Ganhou!\033[m')
    elif player2 == 2:
        print('EMPATE')
    else:
        print('Jogada invalida')
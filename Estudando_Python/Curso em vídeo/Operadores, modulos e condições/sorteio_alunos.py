# choice escolhe 'randomicamente' um item da lista
# import random
# aluno1 = str(input('Digite o nome dos alunos a serem sorteados: '))
# aluno2 = str(input('Digite o nome dos alunos a serem sorteados: '))
# aluno3 = str(input('Digite o nome dos alunos a serem sorteados: '))
# aluno4 = str(input('Digite o nome dos alunos a serem sorteados: '))
# lista = [aluno1, aluno2, aluno3, aluno4]
# escolhido = random.choice(lista)
# print('O aluno escolhido foi: {}'.format(escolhido))

# shuffle serve para 'randomizar' ordem da lista
from random import shuffle
aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
ordem = shuffle(lista)
print('A ordem será {}'.format(lista))

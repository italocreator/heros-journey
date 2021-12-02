# '''fazer um programa que cadastre 4 alunos, receba
# nota de8 avaliações e exiba um grafico '''

import random
import matplotlib.pyplot as plt

nome_alunos = []
for lista_alunos in range(4):
    nome_alunos.append(str(input('Digite o nome dos alunos: ')))

notas_matematica = []

for notas in range(4):
    notas_matematica.append(random.randrange(0, 11))

print(f'A nota do aluno {nome_alunos[0]} foi {notas_matematica[0]} ')
print(f'A nota do aluno {nome_alunos[1]} foi {notas_matematica[1]} ')
print(f'A nota do aluno {nome_alunos[2]} foi {notas_matematica[2]} ')
print(f'A nota do aluno {nome_alunos[3]} foi {notas_matematica[3]} ')

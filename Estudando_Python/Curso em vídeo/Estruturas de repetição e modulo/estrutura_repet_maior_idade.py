# quantos maior de idade e quantos menor de idade?
from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pessoas in range(1, 8):
    nascimento = int(input('Em que ano a {}º pessoa nasceu? '.format(pessoas)))
    idade = atual - nascimento
    # print('Essa pessoa tem \033[1;92m{}\033[m anos'.format(idade))
    if idade >= 18:
        maior += 1
        # print('Essa pessoa atingiu a maior idade!')
    else:
        menor += 1
        # print('Ainda não atingiu a maior idade!')
print(
    'Ao todo tivemos \033[1;92m{}\033[m pessoas maior de idade.'.format(maior))
print(
    'E também tivemos \033[1;92m{}\033[m pessoas menor de idade'.format(menor))

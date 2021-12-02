# nome, idade, sexo, analise do grupo
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulher20 = 0
for i in range(1, 5):
    print('-----{}º Pessoa-----'.format(i))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaidade += idade
    if i == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {}'.format(mediaidade))
print('O homem mais velho se chama {} e tem {} anos'.format(
    nomevelho, maioridadehomem))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher20))

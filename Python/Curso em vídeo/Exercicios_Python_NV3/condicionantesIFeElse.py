# car_age = int(input('Digite quantos anos tem o seu carro: '))
# if car_age >= 5:
#     print('Seu carro está velho')
# else:
#     print('Seu carro é semi-novo')

# while executa o input até que a condição seja concluida
nota1 = float(input('Digite sua primeira nota: '))
while nota1 > 10:
    nota1 = float(input('Você digitou uma nota invalida, digite novamente: '))
nota2 = float(input('Digite sua segunda nota: '))
while nota2 > 10:
    nota2 = float(input('Você digitou uma nota invalida, digite novamente: '))
nota3 = float(input('Digite sua teceira nota: '))
while nota3 > 10:
    nota3 = float(input('Você digitou uma nota invalida, digite novamente: '))
nota4 = float(input('Digite sua quarta nota: '))
while nota4 > 10:
    nota4 = float(input('Você digitou uma nota invalida, digite novamente:'))
media = float((nota1 + nota2 + nota3 + nota4) / 4)
if media >= 7:
    print('Parabéns você foi aprovado, sua média é: {}'.format(media))
else:
    print('Reprovado, sua média foi: {} Estude mais e tente novamente!'.format(media))

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
    nota4 = float(input('Você digitou uma nota invalida, digite novamente: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
if media < 5:
    print('Reprovado! Sua média foi: {} estude mais e tente novamente!'.format(media))
elif media >= 5 and media < 7:
    print('Recuperação!, sua média foi {}.'.format(media))
else:
    print('Parabens! você foi APROVADO! Sua média foi: {}'.format(media))

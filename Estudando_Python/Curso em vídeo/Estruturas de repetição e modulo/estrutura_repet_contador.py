#contador par
soma = 0
for i in range(1, 7):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        soma = soma + num
print('A soma dos valores pares inseridos é: {}'.format(soma))
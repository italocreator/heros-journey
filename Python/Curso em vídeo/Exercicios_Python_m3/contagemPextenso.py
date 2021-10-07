cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um numero entre 0 e 20: '))
while num > 20:
    num = int(input('NUMERO ERRADO! Digite um numero entre 0 e 20: '))
print(f'Você digitou o numero {cont[num]}')

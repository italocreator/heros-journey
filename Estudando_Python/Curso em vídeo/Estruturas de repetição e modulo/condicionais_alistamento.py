from datetime import date
anoatual = date.today().year
dtnasc = int(input('Digite o ano de nascimento: '))
idade = anoatual - dtnasc
print('Quem nasceu em {} tem {} anos em {}.'.format((dtnasc), (idade), (anoatual)))
if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('Você deveria ter se alistado há {} anos.'.format(saldo))
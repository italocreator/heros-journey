#'''Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
vcasa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário atual: '))
tempo = float(input('Digite em quantos anos pretende pagar: '))
parcela = float((vcasa / 12) / tempo)
condi = float(salario * 30 / 100)
if parcela > condi:
    print('Emprestimo negado, sua renda não é compativel')
else:
    print(('Para pagar uma casa de R${} em {} anos a prestação será de R${:.2f}'.format(vcasa, tempo, parcela)))
    print('Empréstimo CONCEDIDO!')
#'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
# mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.'''

velocimetro = float(input('Qual a velocidade do carro: '))
limite = 80
multa = (velocimetro - limite) * 7
if velocimetro > limite:
    print(
        ' \033[1;31mMULTADO!\033[m Você excedeu o limite permitido que é de \033[32m80Km/h\033[m\n',
        'Você deve pagar uma multa de \033[33mR${:.2f}\033[m!\n'.format(multa),
        '\033[1;33mTenha um bom dia! Dirija com segurança!\033[m'
    )
else:
    print(
        '\033[1;33mTenha um bom dia! Dirija com segurança!\033['
    )
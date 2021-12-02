# analise triangulo
# cop = float(input('Digite o valor do cateto oposto: '))
# cad = float(input('Digite os valores do cateto adjacente: '))
# hyp = math.hypot(cad, cop)
# print(
#     'O cateto oposto mede: {}'.format(cop),
#      '\nO cateto adjacente mede: {}'.format(cad),
#      '\nE a hipotenusa mede: {:.2f}'.format(hyp)
# )

# analise angulo, cos, sen, tg
import math
ang = float(input('Digite o angulo que você deseja: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print(
    f'O angulo digitado foi: {ang:.2f}',
    f' \nO seno correspondente a esse angulo: {sen:.2f}',
    f' \nO cosseno correspondente a esse angulo: {cos:.2f}',
    f' \nE a tangente: {tang:.2f}'
)

# transformando float para int no print
# x = float(input('Digite um valor: '))
# print('O valor digitado é {} e a sua porção inteira é: {}'.format(x, int(x)))

# import math
# x = float(input('Digite um valor: '))
# print('O valor digitado é {} e a sua porção inteira é: {}'.format(x, math.trunc(x)))

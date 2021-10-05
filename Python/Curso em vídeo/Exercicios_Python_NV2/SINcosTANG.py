# x = float(input('Digite um valor: '))
# print('O valor digitado é {} e a sua porção inteira é: {}'.format(x, int(x)))

# import math
# x = float(input('Digite um valor: '))
# print('O valor digitado é {} e a sua porção inteira é: {}'.format(x, math.trunc(x)))

# import math


# cop = float(input('Digite o valor do cateto oposto: '))
# cad = float(input('Digite os valores do cateto adjacente: '))
# hyp = math.hypot(cad, cop)
# print(
#     'O cateto oposto mede: {}'.format(cop),
#      '\nO cateto adjacente mede: {}'.format(cad),
#      '\nE a hipotenusa mede: {:.2f}'.format(hyp)
# )

import math
ang = float(input('Digite o angulo que você deseja: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print(
    'O angulo digitado foi: {:.2f}'.format(ang),
    ' \nO seno correspondente a esse angulo é {:.2f}'.format(sen),
    ' \nO cosseno correspondente a esse angulo é {:.2f}'.format(cos),
    ' \nE a tangente: {:.2f}'.format(tang)
)

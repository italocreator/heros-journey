"""
Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu que construísse um programa para verificar,
à partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.

Entrada
A entrada consiste de vários casos de teste. A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de teste.
Cada caso de teste consiste de dois valores A e B maiores que zero, cada um deles podendo ter até 1000 dígitos.

Saída
Para cada caso de entrada imprima uma mensagem indicando se o segundo valor encaixa no primeiro valor, conforme exemplo abaixo.


Exemplo de Entrada	                            Exemplo de Saída
4
56234523485723854755454545478690 78690          encaixa
5434554 543                                     nao encaixa
1243 1243                                       encaixa
54 64545454545454545454545454545454554          nao encaixa

"""


n = int(input())
for i in range(n):
    x, y = input().split()
    teste = 0
    cont = 0
    if len(x) < len(y):
        print("nao encaixa")

    else:
        for j in range(len(y)):
            teste -= 1
            if x[teste] == y[teste]:
                cont += 1

        if cont > 1:
            print("encaixa")

        else:
            print("nao encaixa")

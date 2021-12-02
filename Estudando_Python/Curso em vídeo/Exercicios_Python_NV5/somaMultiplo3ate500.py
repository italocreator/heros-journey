s = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        # print(i)
        cont = cont + 1
        s = s + i
print('A quantidade de termos é: {} E a soma de todos os valores solicitados é {}'.format(cont, s))
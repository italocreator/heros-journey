num = int(input('Digite um numero: '))
print(
    '''Escolha uma das bases para conversão:
    [1] Converter para binário
    [2] Converter para Octal
    [3] Converter para Hexadecimal
    [4] Ambas
''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para Binário é igual a {}'.format(num, bin(num)))
elif opção == 2:
    print('{} convertido para Octal é igual a {}'.format(num, oct(num)))
elif opção == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(num, hex()))
elif opção == 4:
    print('{} convertido para Binário é: {} em Octal é: {} e em Hexadecimal: {}'.format(num, bin(num), oct(num), hex(num)))
else:
    print('Opção invalida!!!')
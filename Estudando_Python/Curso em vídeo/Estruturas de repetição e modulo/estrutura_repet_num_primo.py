# é numero primo ?
num = int(input('Digite um numero: '))
divisiveis = 0
for i in range(1, num+1):
    if num % i == 0:
        divisiveis += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
print('\n\033[mO numero {} foi divisível {} vezes '.format(num, divisiveis))
if divisiveis == 2:
    print('E por isso ele é Primo!')
else:
    print('E por isso ele não é Primo!')

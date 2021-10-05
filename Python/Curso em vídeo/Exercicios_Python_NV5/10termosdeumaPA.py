a = int(input('Primeiro Termo: '))
c = int(input('Razão: '))
dez = a + (11 - 1) * c
for i in range(a, dez, c):
   print('{}'.format(i), end=' → ')
print('FIM')

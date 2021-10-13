pessoas = []
galera = []
contadormaior = contadormenor = 0
for p in range(0, 6):
    pessoas.append(str(input('Nome: ')))
    pessoas.append(int(input('Idade: ')))
    galera.append(pessoas[:])
    pessoas.clear()

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        contadormaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        contadormenor += 1
print(f'Temos {contadormaior} maiores e {contadormenor} menores de idade')

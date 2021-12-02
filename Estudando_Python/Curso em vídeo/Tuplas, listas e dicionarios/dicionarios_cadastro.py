# cadastro nome, sexo, idade, analise do grupo cadastrado
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()  # limpa temporario para armazenar novo cad
    pessoa['nome'] = str(input('Nome: '))  # recebe string em nome
    while True:  # laço m ou F
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! por favor, digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())  # adiciona cad pessoa no dic galera
    while True:  # 1 break somente S ou N, 2 break seguir cadastro ou n
        resposta = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resposta in "SN":
            break
        print('Erro! Responda apenas S ou N')
    if resposta == 'N':
        break
print('-=' * 30)
print(f'Ao todos temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')

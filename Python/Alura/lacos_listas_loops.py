lista_idades = [18, 22, 15, 9, 30, 14]


def verifica_se_pode_dirigir(idade):
    for idade in lista_idades:
        if idade >= 18:
            print(f'{idade} anos de idade, TEM permissão para dirigir')
        else:
            print(f'{idade} anos de idade, NÃO TEM permissão para dirigir')


verifica_se_pode_dirigir(lista_idades)

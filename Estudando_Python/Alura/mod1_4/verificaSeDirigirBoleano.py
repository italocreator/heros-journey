lista_idade = [10, 12, 13, 25, 32, 10, 18]
permissoes = []


def verifica_se_pode_dirigir(lista_idade, permissoes):
    for idade in lista_idade:
        if idade >= 18:
            permissoes.append(True)
        else:
            permissoes.append(False)


verifica_se_pode_dirigir(lista_idade, permissoes)
for permissao in permissoes:
    if permissao == True:
        print(f'Tem permissão para dirigir')
    else:
        print(f'Não tem permissão para dirigir')

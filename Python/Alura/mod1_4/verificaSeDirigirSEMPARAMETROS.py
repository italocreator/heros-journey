def verifica_se_pode_dirigir():
    idade = int(input('idade: '))
    if idade >= 18:
        print('Pode dirigir')
    else:
        print('Não pode dirigir')


verifica_se_pode_dirigir()

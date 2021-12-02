def fatorial(n, show=False):
    """
    ->Calcula o Datorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c} x ')
        f *= c
    return f


# Programa Principal
print(fatorial(5, show=True))

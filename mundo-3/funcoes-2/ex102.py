def fatorial(n, show=False):
    """
    Calcula o fatorial de um número.
    Sobre os parametros:
    :param n: Numero que sera o fatorial.
    :param show: (opcional) Mostra o processo de fatoracao.
    :return: Retorna o valor do fatorial.
    """
    fator = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fator *= c
    return fator

# Programa Principal
print('-=' * 20)
print(fatorial(5, True))
# help(fatorial)
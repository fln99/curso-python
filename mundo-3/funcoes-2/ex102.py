def fatorial(n, s = False):
    """
    Calcula o fatorial de um número.
    Sobre os parametros:
    n - Numero que sera o fatorial.
    s - Mostra o processo de fatoracao.
    """
    fator = 1
    if s == True:
        for c in range(n, 0, -1):
            fator *= c
            if s == True:
                print(c, end=' ')
        print('=', fator)
    else:
        for c in range(n, 0, -1):
            fator *= c
        print(fator)

print('-=' * 20)
fatorial(5, True)
fatorial(5)
# help(fatorial)
def fatorial(n = 1):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f

n = int(input('Digite um número para o fatorial: '))
print('O fatoral de {} é igual a {}'.format(n, fatorial(n)))
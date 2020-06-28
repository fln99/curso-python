def leiaInt(item):
    """
    :param item: Mensagem a ser mostrada no output
    :return: O valor inserido pelo usuário
    """
    ok = False
    valor = 0
    while True:
        n = str(input(item))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO - Digite um número inteiro válido!')
        if ok:
            break
    return valor

# Programa Principal
n = leiaInt('Insira um número: ')
print(f'O número que você digitou é {n}')
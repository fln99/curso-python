def leiaInt(item):
    if item.isnumeric:
        return int(input(item))
    else:
        print('Erro - Digite um número válido!')


# Programa principal
n = leiaInt('Insira um número: ')
print(f'O número que você digitou é {n}')
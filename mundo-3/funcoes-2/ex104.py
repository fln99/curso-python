def leiaInt(item):
    num = int(input(item))
    if num == 0 or num == '':
        return 'ERRO'
    else:
        return num


# Programa principal
n = leiaInt('Insira um número: ')
print(f'O número que você digitou é {n}')
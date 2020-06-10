print('Calcule o fatorial de um número abaixo:')
num = int(input('Insira um número inteiro: '))

controle = num + 1
m = 1

while controle != 1:
    controle -= 1
    m = m * controle
    print(controle)

print('O fatorial de {} é {}!'.format(num, m))
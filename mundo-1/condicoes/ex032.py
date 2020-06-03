print('__- Cálculo de ano Bissexto -__')

ano = int(input('Qual ano você deseja verificar? '))

bissexto = False

if ano % 4 == 0 and (ano % 100 or ano % 400 == 0):
    print('{} é um ano bissexto!'.format(ano))
else:
    print('{} não é um ano bissexto :('.format(ano))
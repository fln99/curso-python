n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

m = (n1 + n2) / 2

print('Sua média foi: {}!'.format(m))

print('Parabéns!' if m >= 6 else 'Estude mais!')
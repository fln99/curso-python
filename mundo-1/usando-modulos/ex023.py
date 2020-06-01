numero = int(input('Insira um número de 0 a 9999: '))

u = str(numero % 10 / 1000).replace('.', '')
d = str(numero % 100 / 1000).replace('.', '')
c = str(numero % 1000 / 1000).replace('.', '')
m = str(numero % 10000 / 1000).replace('.', '')

print('Sobre o número inserido: ')
print('Milhar: {} \nCentena: {} \nDezena: {} \nUnidade: {}'.format(m, c, d, u))
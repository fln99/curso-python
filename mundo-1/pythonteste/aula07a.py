n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
dr = n1 % n2

print('Soma dos números: {}\nMultiplicação: {}\nDivisão: {:.3f}\n'.format(s, m, d), end='')
print('Divisão inteira: {} e Resto da divisão: {}'.format(di, dr))
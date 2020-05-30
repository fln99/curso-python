num = int(input('Insira um número: '))

doub = num * 2
trip = num * 3
sqrt = num ** 0.5

print('Algumas operações com o seu número', end=' >>> ')
print('O dobro de {} é {}, o triplo {} e a raiz quadradra {:.2f}'.format(num, doub, trip, sqrt))
num = int(input('Insira um número inteiro: '))

if num % num == 0 and num % 1 == 0 and num % 2 != 0:
    print('É um número primo!')
else:
    print('Não é número primo.')
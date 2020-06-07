num_1 = int(input('Insira um número inteiro: '))
num_2 = int(input('Insira outro número inteiro: '))

if num_1 > num_2:
    print('O primeiro valor é maior!')
elif num_2 > num_1:
    print('O segundo valor é maior!')
elif num_1 == num_2:
    print('Os dois valores tem o mesmo valor.')
else:
    print('Erro de leitura :(')
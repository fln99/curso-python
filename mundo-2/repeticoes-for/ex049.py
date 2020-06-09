num = int(input('Insira o número da tabuada que desejas: '))

for i in range(1, 11):
    print('{} x {:<2} = {}'.format(num, i, num * i))
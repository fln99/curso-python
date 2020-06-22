matriz = []

for i in range(0, 9):
    numero = int(input('Insira um número: '))
    matriz.append([numero])

cont = 0

for cel in matriz:
    print(f'[ {cel[0]} ]', end='')
    cont += 1
    if cont == 3:
        cont = 0
        print()
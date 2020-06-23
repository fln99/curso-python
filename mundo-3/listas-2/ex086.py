# Minha solução abaixo:
    # matriz = []

    # for i in range(0, 9):
    #     numero = int(input('Insira um número: '))
    #     matriz.append([numero])

    # cont = 0

    # for cel in matriz:
    #     print(f'[ {cel[0]} ]', end='')
    #     cont += 1
    #     if cont == 3:
    #         cont = 0
    #         print()
    
# Solução do Guanabara:
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))

print('=-' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^6}]', end='')
    print()
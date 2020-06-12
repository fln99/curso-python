while True:
    print('-' * 29)
    print('{:=^29}'.format(' GERE SUA TABUADA ABAIXO '))
    print('-' * 29)
    n = int(input('Número da tabuada que você quer: '))

    if n > 0:
        for i in range(1, 11):
            print(f'{n} x {i:<2} = {n * i}')
    else:
        break
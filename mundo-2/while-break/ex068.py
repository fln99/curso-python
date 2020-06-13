from random import choice, randint

resultado = ''

h = 0

while True:
    computador = randint(1, 10)
    escolha_pc = choice(['P', 'I'])

    print('-' * 30)

    humano = int(input('Escolha um número entre 1 e 10: '))
    escolha_h = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]

    total = computador + humano
    
    if total % 2 == 0:
        # Se o total dos números jogados for PAR
        resultado = 'P'
        print('O resultado da jogada foi PAR!')
        if escolha_h == resultado:
            print('Você venceu!')
            h += 1
        else:
            print('Você perdeu.')
            break
    else:
        # Se o total dos números jogados for IMPAR
        resultado = 'I'
        print('O resultado da jogada foi IMPAR!')
        if escolha_h == resultado:
            print('Você venceu!')
            h += 1
        else:
            print('Você perdeu.')
            break

print(f'Total de jogadas ganhas: {h}')
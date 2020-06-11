from random import randint

computador = randint(0, 11)

print('{:=^31}'.format(' Jogo da Adivinhação '))
print('{:^32}'.format(' Jogue um número de 0 a 10 '))

palpites = 0

acertou = False

while not acertou:
    jogador = int(input('Número aqui: '))
    palpites += 1

    if jogador == computador:
        acertou = True
        print('Parabéns, você acertou!')
        print('Sua jogada teve {} palpites.'.format(palpites))

    else:
        if jogador < computador:
            print('Mais... Tente denovo.')
        else:
            print('Menos... Tente denovo.')
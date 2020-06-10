from random import randint

computador = randint(0, 11)

print('{:=^31}'.format(' Jogo da Adivinhação '))
print('{:^32}'.format(' Jogue um número de 0 a 10 '))

palpites = 0

while True:
    jogador = int(input('Número aqui: '))
    palpites += 1

    if jogador == computador:
        print('Parabéns, você venceu!')
        print('Sua jogada teve {} palpites.'.format(palpites))
        break
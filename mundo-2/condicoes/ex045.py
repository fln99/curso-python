from random import randint
from time import sleep

print('{:=^40}'.format(' Jogo do Jokenpô '))

jogada_ia = randint(1, 3)

print('Faça sua escolha: ')
escolha = int(input('1 - Pedra\n2 - Papel\n3 - Tesoura\nOpção: '))

print('Jogando...')

sleep(3)

if escolha == jogada_ia:
    print('Parabéns, você ganhou!')
else:
    print('Que pena, tente novamente!')

# Incompleto
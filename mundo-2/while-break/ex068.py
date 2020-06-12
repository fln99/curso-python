from random import randint
from time import sleep
print('<-=-> ' * 10)
print('{:^59}'.format('Jogo do Par ou Ímpar'))
print('{:^59}'.format('Vença a I.A!'))
print('<-=-> ' * 10)

c = h = 0

while c != 5 or h != 5:
    pc_rand = randint(1, 10)

    h_int = int(input('Escolha um número entre 0 a 10: '))
    h_tipo = str(input('Faça sua escolha: [Par/Impar] ')).strip().upper()[0]

    print('-' * 10)

    print(f'Você jogou {h_int} e definiu final de jogo como {h_tipo}')

    print('Jogada da I.A...')

    sleep(2)

    if pc_rand % 2 == 0:
        if h_int % 2 != 0:
            print('Você perdeu! O computador escolheu PAR')
            c += 1
        else:
            print('Empate! Você e o computador jogaram PAR')
    else:
        if h_int % 2 == 0:
            print('Você venceu! O computador escolheu IMPAR')
            h += 1
        else:
            print('Empate! Você e o computador jogaram IMPAR')

print(f'O computador venceu {c} vezes e você {h}!')
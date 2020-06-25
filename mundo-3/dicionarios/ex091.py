from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
# {'jogador1': 2, 'jogador2': 4, 'jogador3': 5, 'jogador4': 10}
ordem = list()
for c in range(1, 5):
    jogadores[f'jogador{c}'] = randint(1, 6)

print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'{"":3} O {k} tirou {v}')
    sleep(1)

print('Ranking dos jogadores:')
ordem = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
# print(ordem)
for i, v in enumerate(ordem):
    print(f'{"":3}{i + 1}º lugar: {v[0]} com {v[1]} pontos')
    sleep(1)
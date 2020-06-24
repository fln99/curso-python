from random import randint
from time import sleep

jogadores = {}
# {'jogador1': 2, 'jogador2': 4, 'jogador3': 5, 'jogador4': 10}
ordem = dict()
for c in range(1, 5):
    jogadores[f'jogador{c}'] = randint(1, 6)

print('Valores sorteados:')
for k, v in jogadores.items():
    sleep(1)
    print(f'{"":3} O {k} tirou {v}')

print('Ranking dos jogadores:')
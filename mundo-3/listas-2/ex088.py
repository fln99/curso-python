from random import sample, randint
from time import sleep

lista_jogos = list()

print('Python Lotéricas')
jogos = int(input('Deseja fazer quantos jogos? '))

for i in range(jogos):
    lista = sample(range(1, 61), 6)
    lista_jogos.append(lista)

for idx, jogo in enumerate(lista_jogos):
    sleep(1)
    print(f'{idx + 1}º jogo: {jogo}')
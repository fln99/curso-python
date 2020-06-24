jogador = dict()
lista_gols = list()
soma_gols = 0

jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
partidas = int(input(f'Partidas jogadas por {jogador["nome"]}: '))

for c in range(0, partidas):
    gols = int(input(f'Gols na partida {c}: '))
    soma_gols += gols
    lista_gols.append(gols)

jogador['gols'] = lista_gols
jogador['total'] = soma_gols

print('=-' * 28)
print(jogador)
print('=-' * 28)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('=-' * 28)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for pos, item in enumerate(jogador['gols']):
    print(f'{"":3} => Na partida {pos}, fez {item} gols')
    
print(f'Foi um total de {jogador["total"]} gols!')
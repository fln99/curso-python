jogador = dict()
gols = list()
jogadores = list()

print('-=-' * 10)
print(f'{"Python Soccer":^30}')
print('-=-' * 10)

while True:
    print('_- Novo Cadastro -_')
    jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    jogador['partidas'] = int(input(f'Partidas jogadas por {jogador["nome"]}: '))

    print('-' * 30)
    for c in range(0, jogador['partidas']):
        gols.append(int(input(f'Gols de {jogador["nome"]} na partida {c}: ')))
    print('-' * 30)

    jogador['gols'] = gols[:]
    gols.clear()
    jogadores.append(jogador.copy())

    continuar = str(input('Deseja continuar? [S/N] ')).strip()
    if continuar in 'Nn':
        break

print('=' * 40)
print(f'{"Tabela de Jogadores":^40}')
print('=' * 40)
print(f'ID{"":2}Nome{"":10}Gols{"":10}Total')

for pos, j in enumerate(jogadores):
    d2 = 14 - len(j['nome'])
    d3 = 14 - len(j['gols'])
    print(f'{pos:>2}{"":2}{j["nome"]}{"":{d2}}{j["gols"]}{"":{d3}}{j["partidas"]}')

print('-=-' * 10)
escolha = int(input('Mostrar informação do jogador (ID / 999 para o programa): '))
print('-=-' * 10)

print(f' --Levantamento do jogador {jogadores[escolha]["nome"]}:')
for pos, i in enumerate(jogadores[escolha]["gols"]):
    print(f'No jogo {pos} fez {i} gols')
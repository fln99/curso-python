def ficha(n='<desconhecido>', g=0):
    print(f'O jogador {n} fez {g} gol(s) na libertadores.')


# Programa Principal
print('-' * 20)
nome = str(input('Nome do jogador: ')).strip().capitalize()
gols = str(input('Total de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome, gols)
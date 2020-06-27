def ficha(n="<desconhecido>", g=0):
    print(f'O jogador {n} fez {g} gol(s) na libertadores.')


print('-' * 20)
nome = str(input('Nome do jogador: ')).strip().capitalize()
gols = int(input('Total de gols: '))
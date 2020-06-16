campeonato_brasileiro = ('Internacional', 'Sport Recife', 'Fluminense', 'Goiás', 'Atlético PR', 'Botafogo', 'Ceará SC', 'Coritiba', 'Atlético MG', 'São Paulo', 'Atlético GO', 'Palmeiras', 'Corinthians', 'Flamengo', 'Santos', 'Fortaleza', 'Bragantino SP', 'Vasco da Gama', 'Grêmio', 'Bahia')

print('-' * 32)
print('Campeonato Brasileiro de Futebol')
print('-' * 32)

print(f'O 5 primeiros colocados são: {campeonato_brasileiro[:5]}\n')
print(f'Os 4 últimos colocados são: {campeonato_brasileiro[-4:]}\n')
print(f'Todos os times em ordem alfabética: {sorted(campeonato_brasileiro)}\n')
print(f'O time do Corinthians está na posição: {campeonato_brasileiro.index("Corinthians")}')
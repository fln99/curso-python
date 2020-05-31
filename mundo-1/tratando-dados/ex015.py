km = float(input('Quantos quilômetros foram percorridos pelo carro? '))
dias = int(input('Alugou o carro por quantos dias? '))

preco_km = km * 0.15
preco_dias = dias * 60

print('Você terá de pagar R${} reais pelo aluguel do carro!'.format(preco_km + preco_dias))
print('-' * 10)
print('Estatísticas: \n{} por {} dia(s) de aluguel. \n{} por {} km rodados.'.format(preco_dias, dias, preco_km, km))
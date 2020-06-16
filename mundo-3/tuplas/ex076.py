produto_custo = ('Caderno', 12, 'Caneta', 2.50, 'Lápis', 2, 'Borracha', 1.60, 'Apontador', 4, 'Estojo', 6, 'Corretivo', 4)

print(' - ' * 10)
print(f'{"PyPaper Store":^30}')
print(' - ' * 10)

for item in range(0, len(produto_custo), 2):
    print(f'{produto_custo[item]:.<23}', end='')
    print(f'R${produto_custo[item + 1]:5.2f}')
    
print(' - ' * 10)
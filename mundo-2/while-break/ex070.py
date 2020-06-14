print('-' * 19)
print('{:^20}'.format('Python Magazine'))
print('-' * 19)

total_compra = mais_mil = 0

ultimo_produto = {}

mais_barato = {}

while True:
    nome_produto = str(input('Nome do produto: ')).strip()
    preco_produto = float(input('Preço do produto: '))
    continuacao = str(input('Deseja continuar comprando? [S/N] ')).strip().upper()[0]

    total_compra += preco_produto
    
    ultimo_produto = {'nome':nome_produto, 'preco':preco_produto}

    if preco_produto < ultimo_produto['preco']:
            mais_barato = {'nome':nome_produto, 'preco':preco_produto}

    if preco_produto > 1000:
            mais_mil += 1

    if continuacao == 'N':
        print(f'O total gasto na compra foi de R${total_compra}!')
        print(f'Há um total de {mais_mil} produtos de mais de R$1000 reais.')
        print(f'o produto mais barato foi {mais_barato}!')
        break
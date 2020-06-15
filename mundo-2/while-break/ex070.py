print('-' * 19)
print('{:^20}'.format('Python Magazine'))
print('-' * 19)

total_compra = maiores_mil = 0

mais_barato = 99999999

while True:
    nome_produto = str(input('Nome do produto: ')).strip().capitalize()
    preco_produto = float(input('Preço do produto: '))
    escolha = str(input('Você quer continuar comprando? [S/N] ')).strip().upper()[0]

    total_compra += preco_produto

    if preco_produto > 1000:
        maiores_mil += 1
    
    if preco_produto < mais_barato:
        mais_barato = preco_produto
        produto = nome_produto

    if escolha == 'N':
        print(f'O total da compra: R${total_compra:.2f}')
        print(f'Sua compra contém {maiores_mil} produtos acima de R$1000 reais')
        print(f'O produto mais barato da sua cesta é {produto} e custa R${mais_barato:.2f}!')
        break
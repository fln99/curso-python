print('-' * 19)
print('{:^20}'.format('Python Magazine'))
print('-' * 19)

total = mil = menor = 0

nome_p = ''

while True:
    nome = str(input('Qual o nome do produto? ')).strip()
    preco = float(input('Preço do produto: '))
    continuar = str(input('Deseja continuar comprando? [S/N] ')).strip().upper()

    total += preco

    if preco > 1000:
        mil += 1

    menor = preco

    if preco < menor:
        menor = preco
        nome_p = nome

    if continuar in 'Nn':
        break

print(f'O total da compra é R${total:.2f}. Existem {mil} produtos que custam mais de R$1000')
print(f'O produto mais barato é {nome_p} e custa R${menor}!')
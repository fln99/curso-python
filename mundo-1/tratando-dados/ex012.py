price = float(input('Preco produto que deseja comprar = '))

new_price = price - (price * 0.05)

print('Voce ganhou um desconto de 5%!')
print('O valor final do produto sera R${} reais.'.format(new_price))
print('-+-' * 10)
print('{:^30}'.format('Magazine Pythoniza'))
print('-+-' * 10)

preco = float(input('Preço do produto que deseja adquirir: '))

print('Escolha um método de pagamento: ')
metodo = int(input('1 - À vista no cheque ou dinheiro\n2 - À vista no cartão\n3 - 2x no cartão\n4 - 3x ou mais\nOpção: '))

a_vista = preco - (preco * 0.10)
a_vista_cartao = preco - (preco * 0.05)
# 2 vezes é preço normal
parcelas = preco - (preco * 0.20)

if metodo == 1:
    print('Você ganhou 10% de desconto!')
    print('Preço do produto: R${} reais'.format(a_vista))
elif metodo == 2:
    print('Você ganhou 5% de desconto.')
    print('Total a pagar: R${} reais!'.format(a_vista_cartao))
elif metodo == 3:
    print('Total sem desconto.')
else:
    print('Você ganhou 20% de desconto!')
    print('Total a pagar: R${} reais.'.format(parcelas))
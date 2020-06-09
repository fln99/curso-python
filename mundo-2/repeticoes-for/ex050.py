soma = 0
for i in range(0, 6):
    n = int(input('Insira um número inteiro: '))
    if n % 2 == 0:
        soma += n
print('A soma de todos os números pares digitados é de {}!'.format(soma))
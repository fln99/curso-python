n = 0
soma = 0
quant = 0
while n != 999:
    n = int(input('Insira um número inteiro: '))
    if n == 999:
        soma = soma + 0
    else:
        soma = soma + n
        quant = quant + 1
print('A soma dos números inseridos é {}!'.format(soma))
print('Foram inseridos {} números!'.format(quant))
n = soma = cont = 0
n = int(input('Insira um número inteiro: '))

while n != 999:
    soma += n
    cont += 1
    n = int(input('Insira um número inteiro: '))

print('A soma dos números inseridos é {}!'.format(soma))
print('Foram inseridos {} números!'.format(cont))
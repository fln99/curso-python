soma = quant = menor = maior = 0
limite = 5

while limite == limite:
    n = int(input('Insira um número inteiro: '))
    
    soma += n
    quant += 1

    if quant == limite:
        perg = input('Você quer continuar o programa? [S/N] ').upper()
        if perg == 'S' or perg == '' or perg.isnumeric:
            limite += 5
            continue
        else:
            print('A média entre todos os {} números inseridos foi '.format(quant), end=' >>> ')
            print('{}!'.format(soma / quant))
            print('O maior número é {}, enquanto o menor é {}!'.format(maior, menor))
            break
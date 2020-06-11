from time import sleep

n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))

opcao = 0

while opcao != 5:
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa
    ''')

    opcao = int(input('O que deseja fazer? '))

    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}!'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        produto = n1 * n2
        print('O produto de {} e {} é {}!'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior valor é {}.'.format(maior))
    elif opcao == 4:
        print('Informe os números novamente!')
        n1 = int(input('Insira o primeiro valor: '))
        n2 = int(input('Insira o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida!')
    sleep(2)
print('Final do programa.')
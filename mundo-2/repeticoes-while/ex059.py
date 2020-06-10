while True:
    print(('-' * 20), end=' ')
    print('Start')
    n1 = int(input('Insira o primeiro valor: '))
    n2 = int(input('Insira o segundo valor: '))

    print('Escolha a operação a ser feita com os dados:')
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa
    ''')

    opcao = int(input('O que deseja fazer? '))

    if opcao == 1:
        print('A soma entre {} e {} é igual a {}!'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('A multiplicação entre os valores resultou em: {}!'.format(n1 * n2))
    elif opcao == 3:
        tipo = ''
        valor = 0
        if n1 > n2:
            valor = n1
            tipo = 'maior'
        else:
            valor = n2
            tipo = 'menor'
        print('O {} valor inserido foi: {}!'.format(tipo, valor))
    elif opcao == 4:
        print('Reiniciando o programa...')
    else:
        print('Você acaba de sair do programa!')
        break
lista_numeros = []

cont = 0

while True:
    cont += 1
    numero = int(input('Insira um número inteiro: '))

    if numero not in lista_numeros:
        lista_numeros.append(numero)
        index = lista_numeros.index(numero)
        print('Valor adicionado à ultima posição da lista!')

        if numero > lista_numeros[index]:
            print('Valor adicionado à ultima posição!')
    
    if cont == 3:
        continuar = str(input('Deseja continuar? '))

        if continuar in 'Nn':
            break
        else:
            cont = 0
    
print(lista_numeros)
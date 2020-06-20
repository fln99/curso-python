lista_numeros = []

while True:
    numero = int(input('Insira um número: '))

    if numero == -1:
        break

    if len(lista_numeros) == 0: # Se a lista estiver vazia, insere um novo valor
        lista_numeros.append(numero)

    elif numero > lista_numeros[0]: # Caso o segundo número inserido for maior que o primeiro, adiciona ele a ultima posição
        lista_numeros.insert(-1, numero)

    elif numero < lista_numeros[0]:
        lista_numeros.insert(0, numero)

    elif numero < lista_numeros[-1] and numero > lista_numeros[0]:
        lista_numeros.insert(1, numero)

print(lista_numeros)
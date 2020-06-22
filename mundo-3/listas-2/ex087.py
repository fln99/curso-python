matriz = []
pares = soma_terc = cont = maior = menor = 0
# Possibilita a inserção de 9 números na lista;
for i in range(0, 9):
    numero = int(input('Insira um número: '))
    if numero % 2 == 0:
        pares += numero
    matriz.append([numero])

print('=-' * 10)
# Gera a matriz a partir dos elementos contidos na lista;
for cel in matriz:
    print(f'[ {cel[0]} ]', end='')
    cont += 1
    if cont == 3:
        cont = 0
        print()
# Soma a 3ª coluna inteira;
for cel in range(0, len(matriz), 3):
    soma_terc += matriz[cel + 2][0]
# Maior valor da 2ª linha;
segunda_linha = matriz[3:6]
for c in range(0, 3):
    if maior < segunda_linha[c][0]:
        maior = segunda_linha[c][0]
    else:
        menor = segunda_linha[c][0]
print('=-' * 10)
print(f'Os números pares da sua matriz, somados irão resultar em {pares}!')
print(f'A soma dos itens na 3ª coluna resultará em: {soma_terc}')
print(f'O maior valor da 2ª linha é {maior}!')
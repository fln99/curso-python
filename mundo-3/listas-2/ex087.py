matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = maior = soma = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))

print('=-' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^6}]', end='')
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
    print()
print('=-' * 20)
print(f'A soma dos valores pares é {pares}')
for linha in range(0, 3):
    soma += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {soma}')
for c in range(0, 3):
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')
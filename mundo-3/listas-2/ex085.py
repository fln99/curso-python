numeros = [[], []]
for p in range(0, 7):
    numero = int(input(f'Digite o {p + 1}º valor: '))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)
print('=-' * 20)
print(f'A lista de pares é {sorted(numeros[0])}')
print(f'A lista de ímpares é {sorted(numeros[1])}')
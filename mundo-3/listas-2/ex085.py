numeros = [[], []]

for p in range(0, 7):
    numero = int(input('Insira um número: '))
        
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)
    
numeros.sort()

print('=-' * 20)
print(f'A lista de pares é {numeros[0]}')
print(f'A lista de ímpares é {numeros[1]}')
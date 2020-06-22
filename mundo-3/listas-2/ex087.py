matriz = [[], [], [], [], [], [], [], [], []]

soma = 0

for cell in matriz:
    valor = int(input('Insira um valor: '))
    if valor % 2 == 0:
        soma += valor

    cell.append(valor)

print(matriz)
print(f'A soma dos valores pares da matriz é {soma}!')
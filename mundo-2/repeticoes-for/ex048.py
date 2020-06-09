soma = 0
for i in range(1, 501):
    if i % 3 == 0 and i % 2 != 0:
        # print(i)
        soma += i

print('A soma de todos os números ímpares no intervalo de 1 até 500 é:')
print(soma)
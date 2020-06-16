num_1 = int(input('Insira um número: '))
num_2 = int(input('Insira mais um número: '))
num_3 = int(input('Insira outro número: '))
num_4 = int(input('Insira mais outro número: '))

tupla_numeros = (num_1, num_2, num_3, num_4)

pares = ''

for num in tupla_numeros:
    if num % 2 == 0:
        pares += str(f'{num:<3}')

indice_3 = 0

if 3 in tupla_numeros:
    indice_3 = tupla_numeros.index(3)

print(f'A tupla resultante é: {tupla_numeros}')
print(f'O número 9 apareceu {tupla_numeros.count(9)} vezes')
print(f'O valor 3 aparece na posição {indice_3}')
print(f'Os valores pares na tupla são:  {pares}')
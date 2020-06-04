num_1 = int(input('Primeiro número: '))
num_2 = int(input('Segundo número: '))
num_3 = int(input('Terceiro número: '))

# Verificando quem é maior:

menor = num_1

if num_2 < num_1 and num_2 < num_3:
    menor = num_2

if num_3 < num_1 and num_3 < num_2:
    menor = num_3

# Verificando quem é o menor:

maior = num_1

if num_2 > num_1 and num_2 > num_3:
    maior = num_2

if num_3 > num_1 and num_3 > num_2:
    maior = num_3

print('O maior valor é {} e o menor é {}!'.format(maior, menor))
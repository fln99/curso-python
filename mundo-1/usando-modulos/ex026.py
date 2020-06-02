frase = input('Insira uma frase aqui > ')

total_a = frase.count('a')

print('A sua frase contém {} letras "a"'.format(total_a))

primeiro_a = frase.find('a')
ultimo_a = frase[-1].find('a')

print('A primeira aparece na posição {} e a última na {}!'.format(primeiro_a, ultimo_a))
print('Verificador de Palíndromo!')
print('''
Palíndromo é uma frase que tem o mesmo sentido em ambas as direções.
Ex: APOS A SOPA = APOS A SOPA
    A TORRE DA DERROTA
    A SACADA DA CASA
''')
frase = (str(input('Insira a frase: ')).strip()).replace(' ', '')

size = len(frase)

for i in range(size):
    # print(frase[i])
    if frase[0] == frase[-1]:
        print(frase[0], frase[-1])

        if frase[i] == frase[-(i + 1)]:
            print(frase[i], frase[(- i + 1)])
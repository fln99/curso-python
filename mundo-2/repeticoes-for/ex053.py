print('Verificador de Palíndromo!')
print('''
Palíndromo é uma frase que tem o mesmo sentido em ambas as direções.
Ex: APOS A SOPA = APOS A SOPA
    A TORRE DA DERROTA
    A SACADA DA CASA
''')

frase = (str(input('Insira a frase: ')).strip()).replace(' ', '').upper()

inverso = frase[::-1]

if inverso == frase:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
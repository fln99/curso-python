frase = str(input('Insira uma frase aqui > ')).upper().strip()

print('A sua frase contém {} letras "a"'.format(frase.count('A')))

print('A primeira aparece na posição {} e a última na {} posição!'.format(frase.find('A') + 1, frase.rfind('A') + 1))
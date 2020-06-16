extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 
            'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quatorze', 'quinze', 
            'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

numero = int(input('Insira um número: '))

while True:
    if numero < 0 or numero > 20:
        numero = int(input('Insira um número novamente. Entre 0 e 20: '))
    else:
        break

print(f'Você acabou de digitar o número {extenso[numero]}')
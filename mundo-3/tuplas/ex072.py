extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
            'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quatorze', 'quinze', 
            'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

numero = int(input('Insira um número: '))

while True:
    if 0 < numero > 20:
        numero = int(input('Insira um número novamente. Entre 0 e 20: '))

    else:
        print(f'Você acabou de digitar o número {extenso[numero]}')
        continuar = str(input('Você quer continuar? [S/N] '))

        if continuar in 'Ss':
            numero = int(input('Insira um número: '))
        else:
            break
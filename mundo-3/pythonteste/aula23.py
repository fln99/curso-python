# Sobre a estrutura simples do try.
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print('Infelizmente ocorreu um erro!')
    print(f'Tipo do erro: {erro.__class__}')
else:
    print(f'O resultado da divisão é {r}')
finally:
    print(f'É com satisfação que lhe desejamos uma boa semana :D')
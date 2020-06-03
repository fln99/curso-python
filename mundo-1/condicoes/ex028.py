from random import randint

print('--- Desafio do Jarv.is ---')
print('Tente adivinhar o número que o computador gerou!')

palpite = int(input('Insira um número inteiro de 0 a 5 como palpite: '))

aleatorio = randint(0, 5)

if palpite == aleatorio:
    print('Você acertou e venceu o desafio! PARABÉNS!')
else:
    print('Tente novamente, ninguém me vence hahaha >:O')

print('The end...')
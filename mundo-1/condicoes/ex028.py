from random import randint
from time import sleep

print('--- Desafio do Jarv.is ---')
print('Tente adivinhar o número que o computador gerou!')

aleatorio = randint(0, 5)

palpite = int(input('Insira um número inteiro de 0 a 5 como palpite: '))

print('Fazendo a verificação...')

sleep(2)

if palpite == aleatorio:
    print('Você acertou e venceu o desafio! PARABÉNS!')
else:
    print('Tente novamente, ninguém me vence hahaha >:O')
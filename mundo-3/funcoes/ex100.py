from random import randint
from time import sleep

def sorteia(lis):
    print('Sorteio de 5 números da lista: ', end='')
    for c in range(0, 5):
        n = randint(1, 10)
        lis.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('Finalizado!')


def soma_par(lis):
    soma = 0
    for n in lis:
        if n % 2 == 0:
            soma += n
    print(f'Somando todos os valores pares em {lis} teremos {soma}')

numeros = list()
sorteia(numeros)
soma_par(numeros)
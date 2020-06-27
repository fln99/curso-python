from time import sleep

def mostrador(item):
    print(item)

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
        
    print('-' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
print('-' * 20)
print('Insira uma contagem personalizada:')
ini = int(input('Início da contagem: '))
fim = int(input('Fim da contagem: '))
passo = int(input('Passo para a contagem: '))
contador(ini, fim, passo)
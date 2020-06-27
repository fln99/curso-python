from time import sleep

def maior(* num):
    cont = maior = 0
    print('-' * 20)
    print('Analisando os valores passados...')
    for n in num:
        print(n, end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1
    print(f'Foram informados {cont} valores.')
    print(f'E o maior valor informado foi {maior}.')

maior(10, 2, 9, 10)
maior(1, 6, 22, 6, 12, 5)
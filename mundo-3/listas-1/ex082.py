lista = []
lista_par = []
lista_impar = []

while True:
    numero = int(input('Insira um número: '))
    lista.append(numero)

    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)

    escolha = str(input('Deseja continuar? [S/N] '))
    if escolha in 'Nn':
        break

print(f'Se liga na lista que tu gerou -> {lista}')
print(f'Os números pares dela são: {lista_par}')
print(f'Os números ímpares são: {lista_impar}')
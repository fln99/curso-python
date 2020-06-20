lista_num = []

while True:
    numero = int(input('Insira um valor: '))

    if numero not in lista_num:
        lista_num.append(numero)

    continuar = str(input('Quer continuar? ')).strip().upper()

    if continuar in 'Nn':
        break

print(f'Lista gerada com seus números: {sorted(lista_num)}')
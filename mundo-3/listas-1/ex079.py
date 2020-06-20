lista_num = []

while True:
    numero = int(input('Insira um valor: '))
    if numero not in lista_num:
        lista_num.append(numero)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado. Use outro nome!')

    continuar = str(input('Quer continuar? ')).strip().upper()
    if continuar in 'Nn':
        break

print('=-' * 25)
lista_num.sort()
print(f'Lista gerada com seus números: {lista_num}')
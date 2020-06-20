lista = list()

while True:
    numero = int(input('Insira um número: '))
    lista.append(numero)

    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break

print(f'Foram inseridos {len(lista)} números na lista!')
print(f'Valores em ordem decrescente: {lista.sort(reverse=True)}')
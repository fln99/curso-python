lista = []

while True:
    lista.append(int(input('Insira um número: ')))

    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break

print(f'Foram inseridos {len(lista)} números na lista!')
print(f'Valores em ordem decrescente: {list(reversed(lista))}')
print(f'O valor 5 se encontra na lista!' if 5 in lista else 'O número 5 não foi encontrado na lista!')

lista = list()

while True:
    lista.append(int(input('Insira um número inteiro: ')))
    print(lista)

    escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()

    if escolha in 'Nn':
        break

cont = 0

quantos_maiores_iguais = lista.count(max(lista))
indice_do_primeiro = lista.index(max(lista))

while cont <= quantos_maiores_iguais:
    print(lista.index(max(lista), cont))
    cont += 1

# print(f'O maior valor da lista é {max(lista)} e se encontra na posição {lista.index(max(lista))}!')
# print(f'O menor valor da lista é {min(lista)} e se encontra na posição {lista.index(min(lista))}!')
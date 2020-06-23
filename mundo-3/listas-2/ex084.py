pessoas = list()
pessoa = list()
maior = menor = 0

while True:
    pessoa.append(str(input('Informe seu nome: ')).strip().capitalize())
    pessoa.append(float(input('Informe seu peso: ')))
    if len(pessoas) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    pessoas.append(pessoa[:])
    pessoa.clear()

    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas na lista!')
print(f'As pessoas com {maior} são: ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'As pessoas com {menor} são: ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()
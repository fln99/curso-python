pessoas = list()
pessoa = list()

while True:
    pessoa.append(str(input('Informe seu nome: ')).strip().capitalize())
    pessoa.append(float(input('Informe seu peso: ')))

    pessoas.append(pessoa[:])
    pessoa.clear()

    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break

maior = menor = 0
maior_peso = list()
menor_peso = list()

for c in pessoas:
    if c == 0:
        maior = menor = 0
    if c[1] > maior:
        maior = c[1]
    else:
        menor = c[1]

for c in pessoas:
    if c[1] == maior:
        maior_peso.append(c[0])
    elif c[1] == menor:
        menor_peso.append(c[0])

print(f'Foram cadastradas {len(pessoas)} pessoas na lista!')
print(f'As pessoas com {maior} são: {maior_peso}')
print(f'As pessoas com {menor} são: {menor_peso}')
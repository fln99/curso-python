pessoas = list()
pessoa = dict()
soma_idades = 0

while True:
    pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().capitalize()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('[Erro] - Insira apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma_idades += pessoa['idade']
    pessoas.append(pessoa.copy())
    pessoa.clear()
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).strip().capitalize()[0]
        if continuar in 'SN':
            break
        print('[ERRO] - Insira apenas S ou N.')
    if continuar in 'Nn':
        break

media = soma_idades / len(pessoas)

print('=-' * 20)
print(f' - O grupo tem um total de {len(pessoas)} pessoas')
print(f' - A média de idade é {media} anos')
print(f' - As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()

print(f' - Pessoas acima da média: ')
for p in pessoas:
    if p['idade'] > media:
        print(f"{'':5}Nome = {p['nome']}, Sexo = {p['sexo']}, Idade = {p['idade']}")
        
print('<<< Fim do Programa >>>')
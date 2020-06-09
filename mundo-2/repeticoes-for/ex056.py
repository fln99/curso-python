s_idade = 0
controle = 0
mais_velho = {'nome':'', 'idade':0}
menores_20 = 0

for i in range(0, 4):
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    genero = str(input('Gênero (M ou F): ')).strip().lower()
    s_idade += idade

    if genero == 'm':
        if controle == 0:
            controle = idade
        if idade > controle:
            mais_velho['nome'] = nome
            mais_velho['idade'] = idade
    else:
        if idade < 20:
            menores_20 += 1
media = s_idade / 4

print('A média das idades cadastradas é {} anos!'.format(media))
print('A pessoa mais velha é {} com {} anos de idade!'.format(mais_velho['nome'], mais_velho['idade']))
print('O total de garotas menores de 20 é {}!'.format(menores_20))
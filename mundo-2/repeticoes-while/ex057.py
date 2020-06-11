genero = str(input('Informe seu gênero: [M/F] ')).strip().upper()[0]

while genero not in 'MF':
    genero = str(input('Dado inválido. Informe seu gênero novamente: [M/F] ')).strip().upper()[0]
print('{} registrado com sucesso!'.format(genero))
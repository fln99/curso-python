total18 = total_h = totalM20 = 0

while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Seu sexo: [M/F] ')).strip().upper()[0]

    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        total_h += 1
    if sexo == 'F' and idade < 20:
        totalM20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resp == 'N':
        break
print(f'Total de pessoas maiores de 18: {total18}')
print(f'Temos {total_h} homens cadastrados!')
print(f'E mulheres abaixo dos 20 anos temos {totalM20}')
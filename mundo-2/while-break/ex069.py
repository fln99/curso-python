maior = qtd_h = qtd_m = 0

while True:
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Quantos anos você tem? '))
    sexo = str(input('Qual seu sexo? [M/F] ')).strip().upper()

    encerrar = str(input('Você quer continuar? [S/N] ')).strip().upper()

    if idade >= 18:
        maior += 1
    if sexo == 'M':
        qtd_h += 1
    if sexo == 'F' and idade <= 20:
        qtd_m += 1

    if encerrar in 'Nn':
        print(f'Existem {maior} pessoas maiores de 18\n{qtd_h} homens cadastrados\n{qtd_m} mulheres menores de 20 anos!')
        break
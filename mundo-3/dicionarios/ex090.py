boletim = dict()

for c in range(0, 1):
    boletim['aluno'] = str(input('Nome: ')).strip().capitalize()
    boletim['nota'] = float(input('Média das notas: '))

print(f'O nome do aluno é {boletim["aluno"]}')
print(f'A média das notas de {boletim["aluno"]} foi {float(boletim["nota"])}')
print(f'Situação: ', end='')

if boletim['nota'] >= 7:
    print('Aprovado(a)')
elif 5 <= boletim['nota'] < 7:
    print('Recuperação')
else:
    print('Reprovado(a)')
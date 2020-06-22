lista_boletim = list()

while True:
    nome_aluno = str(input('Nome do aluno: ')).strip().capitalize()
    nota_1_aluno = float(input('Primeira nota: '))
    nota_2_aluno = float(input('Segunda nota: '))

    lista_boletim.append([nome_aluno, [nota_1_aluno, nota_2_aluno]])

    resposta = str(input('Deseja continuar cadastrando notas? [S/N] '))

    if resposta in 'Nn':
        break

print(f'{"Boletim Escolar":^30}')
print('=-' * 15)

print(f'Número{"":5}Nome{"":5}Média')
for id_, aluno in enumerate(lista_boletim):
    print(f'{id_}{"":7}{aluno[0]}{"":7}{(aluno[1][0] + aluno[1][1]) / 2}')

print('=-' * 15)

consulta = int(input('Consulta nota do aluno pelo número: '))
print(f'{lista_boletim[consulta][0]} tirou as seguintes notas: {lista_boletim[consulta][1][0:]}')
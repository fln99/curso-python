from datetime import datetime
ano_atual = datetime.today().year
info = {}

info['nome'] = str(input('Seu nome: ')).strip().capitalize()
ano_nasc = int(input('Ano de nascimento: '))
info['idade'] = ano_atual - ano_nasc
info['ctps'] = int(input('Número da arteira de trabalho (0 caso não tenha): '))

if info['ctps'] != 0:
    info['contrato'] = int(input('Ano de contratação: '))
    info['salario'] = float(input('Salário: R$ '))
    info['aposentadoria'] = (info['contrato'] + 35) - ano_nasc

print('=-' * 20)
print(info)
for k, v in info.items():
    print(f'{k} tem o valor {v}')
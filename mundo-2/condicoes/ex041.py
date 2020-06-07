from datetime import date
ano_atual = date.today().year

ano_nasc = int(input('Seu ano de nascimento aqui: '))

idade = ano_atual - ano_nasc

categoria = ''

if idade <= 9:
    categoria = 'Mirim'
elif idade <= 14:
    categoria = 'Infantil'
elif idade <= 18:
    categoria = 'Junior'
elif idade <= 20:
    categoria = 'Sênio'
else:
    categoria = 'Master'

print('Você se encaixa na categoria {}!'.format(categoria))
from datetime import date

ano_atual = date.today().year

print('-+-' * 14)
print('{:^40}'.format('Exército do Python'))
print('Consulte a situação de teu alistamento!')
print('-+-' * 14)

ano_nasc = int(input('Ano de seu nascimento: '))

idade_usuario = ano_atual - ano_nasc

if idade_usuario > 18:
    print('Você se alistou ou deveria ter se alistado a {} ano(s) atrás!'.format(idade_usuario - 18))
elif idade_usuario == 18:
    print('Você deve se alistar este ano! Não atrase ou será multado.')
elif idade_usuario < 18:
    print('Você deverá se alistar daqui {} ano(s)!'.format(18 - idade_usuario))
    print('Fique atento ao calendário!')

print('Deixe seu feedback no nosso site!')
from datetime import date

ano_atual = date.today().year

quant_maiores = 0
quant_menores = 0

for i in range(0, 7):
    ano_nasc = int(input('Seu ano de nascimento: '))
    if ano_atual - ano_nasc >= 18:
        quant_maiores += 1
    else:
        quant_menores += 1
        
print('{} pessoas já são maiores de idade e {} menores.'.format(quant_maiores, quant_menores))
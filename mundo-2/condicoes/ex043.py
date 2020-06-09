print(':-:' * 10)
print('{:^30}'.format('Cálculo de IMC'))
print(':-:' * 10)

peso = float(input('Seu peso: '))
altura = float(input('Sua altura em metros: '))

IMC = peso / pow(altura, 2)

situacao = '';

if IMC < 18.5:
    situacao = 'Magreza'
elif IMC <= 24.9:
    situacao = 'Normal'
elif IMC <= 29.9:
    situacao = 'Sobrepeso'
elif IMC <= 39.9:
    situacao = 'Obesidade'
else:
    situacao = 'Obesidade Grave'

print('Seu IMC resultou em {:.2f}! Caracterizado como {}.'.format(IMC, situacao))
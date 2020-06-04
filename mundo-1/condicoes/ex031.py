print('Diamante Negro Viagens! Consulte preços abaixo: ')

distancia = float(input('Quantos quilômetros de distância tem seu destino? '))

if distancia <= 200:
    print('Você pagará R${:.2f} reais por {} Km!'.format(distancia * 0.50, distancia))
else:
    print('Você pagará R${:.2f} reais por {} Km!'.format(distancia * 0.45, distancia))
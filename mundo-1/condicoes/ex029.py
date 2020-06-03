velocidade = float(input('Seu carro está em que velocidade? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7.00
    print('Você está sendo MULTADO em R${:.2f} reais por exceder a velocidade de 80Km/h!'.format(multa))
else:
    print('Velocidade segura! Parabéns, você é consciente! :D')
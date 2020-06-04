print('Faça você mesmo o seu triângulo!')

lado_1 = float(input('Insira lado A: '))
lado_2 = float(input('Insira lado B: '))
lado_3 = float(input('Insira lado C: '))

if ((lado_2 - lado_3) < lado_1 < (lado_2 + lado_3)):
    print('Seu triângulo poderá ser construído!')
else:
    print('Seu triângulo não poderá ser construído!')
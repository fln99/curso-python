salario_func = float(input('Quantos reais você ganha? '))

if salario_func >= 1250:
    print('Você ganhou um aumento de 10%!')
    print('A partir de agora você receberá R${} reais.'.format(salario_func + (salario_func * 0.10)))
else:
    print('Você ganhou um aumento de 15%!')
    print('A partir de agora você receberá R${} reais.'.format(salario_func + (salario_func * 0.15)))
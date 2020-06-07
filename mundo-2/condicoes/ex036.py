print('-+-' * 6)
print('Python Empréstimos')
print('-+-' * 6)

valor_casa = float(input('Valor da casa: '))
salario_comprador = float(input('Salário do comprador: '))
tempo_anos = int(input('Deseja parcelar em quantos anos? '))

valor_mensal = valor_casa / (tempo_anos * 12) # Anos para meses
limite = salario_comprador * 0.30

if valor_mensal >= limite:
    print('Seu empréstimo foi negado!')
    print('Motivo: valor mensal excede o salário.')
    print('Valor mensal do empréstimo: R${} reais. Porcentagem do salário: R${} reais'.format(valor_mensal, limite))
elif valor_mensal <= limite:
    print('Seu empréstimo foi aprovado. Parabéns!')
    print('Você tem um total de {} parcelas de R${} reais!'.format(tempo_anos * 12, valor_mensal))
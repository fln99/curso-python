print('-' * 30)
print('{:^30}'.format('$ PythonBank $'))
print('-' * 30)

valor = int(input('Qual o valor a ser sacado? R$'))
total = valor 
cedula = 50
tot_cedulas = 0
while True:
    if total >= cedula:
        total -= cedula
        tot_cedulas += 1
    else:
        if tot_cedulas > 0:
            print(f'Total de {tot_cedulas} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        tot_cedulas = 0
        if total == 0:
            break
print('<->' * 10)
print('Volte sempre :)')
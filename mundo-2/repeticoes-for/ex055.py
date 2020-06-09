maior_peso = 0
menor_peso = 0
controle = 0

for i in range(0, 5):
    peso = float(input('Insira seu peso aqui: '))

    if controle == 0:
        controle = peso
    if peso > controle:
        maior_peso = peso
    else:
        menor_peso = peso

print('O menor peso cadastrado foi {}Kg!'.format(menor_peso), end=' ')
print('Já o maior foi {}Kg!'.format(maior_peso))
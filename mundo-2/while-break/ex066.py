print('{:-^40}'.format('O número 999 cancela o loop!'))
c = s = 0
while True:
    n = int(input('Insira um número: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Foram inseridos {c} números.', end=' ')
print(f'O soma dos números é: {s}')
express = str(input('Insira uma expressão: '))
pilha = list()

for simb in express:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está válida.')
else:
    print('Sua expressão está errada!')
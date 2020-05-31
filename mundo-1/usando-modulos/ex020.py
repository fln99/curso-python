from random import sample

aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')

print('A ordem de apresentação resultou em', end=' >>> ')
print('{}!'.format(sample([aluno1, aluno2, aluno3, aluno4], 4)))
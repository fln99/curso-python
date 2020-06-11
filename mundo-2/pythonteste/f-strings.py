# As f-strings substituem o .format(), responsável por interpolar strings.

nome = 'Felipe'
idade = 20
salario = 985.4

# Versão Python 3
print('Meu nome é {} e tenho {} anos!'.format(nome, idade))

# Versão Python 3.6+ (-+ a versão que lançou a f-string)
print(f'Meu nome é {nome} e tenho {idade} anos!')

# Para definir décimos, espaçamentos:

print(f'{nome:->20} trabalha na FLNCorp há {idade} anos! E recebe R${salario:.3f} de salário')
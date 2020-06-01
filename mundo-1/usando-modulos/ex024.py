nome_cidade = input('Como sua cidade se chama? ')

primeiro_nome = 'santo' in ((nome_cidade.lower().split())[0])

print('Cidade começa com "Santo?" - {}'.format(primeiro_nome))
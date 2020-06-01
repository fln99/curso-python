nome_completo = input('Insira seu nome completo: ')

nome_upper = nome_completo.upper()
nome_lower = nome_completo.lower()

tamanho = len(nome_completo.replace(' ', ''))

tamanho_primeiro_nome = len((nome_completo.split())[0])

print('Seu nome uppercase fica assim', end=' > > ')
print(nome_upper)
print('Seu nome lowercase fica assim', end=' > > ')
print(nome_lower)
print('Seu nome completo tem {} caracteres!'.format(tamanho))
print('Já seu primeiro nome tem {} caracteres.'.format(tamanho_primeiro_nome))
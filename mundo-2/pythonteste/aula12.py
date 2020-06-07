nome = str(input('Qual seu nome? '))

if nome == 'Felipe':
    print('Mas que nome bonito kkkk')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil :)')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino KKKKKKK')
else:
    print('Seu nome é bem normal! :D')

print('Bom dia, {}!'.format(nome))
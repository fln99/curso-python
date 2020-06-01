nome_pessoa = input('Qual seu nome completo? ')

existe = 'silva' in (nome_pessoa.lower())

print('Resultado para a busca do sobrenome "Silva": {}'.format(existe))
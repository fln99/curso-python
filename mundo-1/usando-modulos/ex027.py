nome_completo = input('Insira seu nome completo: ').strip()

slice_nome = nome_completo.split()

print('Seu primeiro nome é: {} e o último: {}'.format(slice_nome[0], slice_nome[-1]))
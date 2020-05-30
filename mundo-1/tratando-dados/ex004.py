st = input('Digite algo: ')

print('Tipo primitivo do dados inserido: {}'.format(type(st)))
print('Contém números? {}'.format(st.isnumeric()))
print('Contém letras e números? {}'.format(st.isalnum()))
print('Contém somente letras? {}'.format(st.isalpha()))
print('Todo em letras maiúsculas? {}'.format(st.isupper()))
print('Todo em letras minúsculas? {}'.format(st.islower()))
print('Primeira letra de palavra em maiúsculo? {}'.format(st.istitle()))
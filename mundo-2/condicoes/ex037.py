# Binário, octal e hexadecimal
numero = int(input('Digite um número inteiro: '))

print('Escolha para qual base numérica quer converter:')
escolha = int(input('1 - Binário\n2 - Octal\n3 - Hexadecimal\nOpção: '))

# O motivo do uso de [2:] é para selecionar apenas o conteúdo depois
# dos primeiros, que servem para mostrar o tipo de base numérica.

if escolha == 1:
    print('Seu número em binário: {:2}'.format(bin(numero)[2:]))
elif escolha == 2:
    print('Seu número em octal é: {:2}'.format(oct(numero)[2:]))
elif escolha == 3:
    print('Seu número em hexadecimal ficou assim: {:2}'.format(hex(numero)[2:]))
else:
    print('OPÇÃO INVÁLIDA!')
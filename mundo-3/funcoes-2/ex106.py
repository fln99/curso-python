from time import sleep

def ajuda(comm):
    help(comm)


def título(msg, color=0):
    tam = len(msg)
    print('-' * tam)
    print(msg)
    print('-' * tam)
    sleep(1)

# Programa Principal
comando = ''
while True:
    título('Sistema de Ajuda - Interactive Help')
    comando = str(input('Função ou Biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('Programa Encerrado')

# OBS: Desafio feito pelo VSCODE, o terminal não aceitou cores.
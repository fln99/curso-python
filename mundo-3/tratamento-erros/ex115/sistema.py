from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'bancodedados.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do sistema'])
    if resposta == 1:
        # Opção que lista o arquivo 
        lerArquivo(arq)
    elif resposta == 2:
        # Opção para fazer o cadastro de um pessoa
        cabecalho('Novo cadastro')
        nome = str(input('Nome da pessoa:'))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema...')
        sleep(2)
        break
    else:
        cabecalho('Opção inválida!')
    sleep(2)
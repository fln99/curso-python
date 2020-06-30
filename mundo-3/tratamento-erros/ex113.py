def common_code(tipoInt, txt):
    """
    Função usada para tipos numéricos inteiros ou flutuantes.
    :param tipoInt: padrão para tipo inteiro
    :param txt: mensagem a ser utilizada no input de 'n'
    :return: retorna n 
    """
    while True:
        try:
            if tipoInt:
                n = int(input(txt))
            else:
                n = float(input(txt).replace(',', '.'))
        except Exception as error:
            print('ERRO! o_o`')
            print(f'Tipo do erro: {error.__class__}')
        except KeyboardInterrupt:
            print('ERRO! x..x')
            print('O usuário encerrou a execução do programa.')
        else:
            break
    return n


def leiaInt(msg):
    return common_code(True, msg)


def leiaFloat(msg):
    return common_code(False, msg)


n_i = leiaInt('Insira um número inteiro: ')
n_f = leiaFloat('Insira um número real: ')

print(f'Você acabou de cadastrar um número inteiro {n_i} e real {n_f}!')
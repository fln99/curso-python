def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, KeyError):
            print('ERRO - Digite um número inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('O usuário interrompeu a entrada de dados.')
            return 0
        else:   
            return n


def linha(tam=42):
    return '-' * 42


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc
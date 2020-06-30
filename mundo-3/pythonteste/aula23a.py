# Estrutura do try com mais de um exception, e este com o determinado erro.
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError): # Utiliza-se parênteses para mais de um exception.
    print('Houve erro de valor/tipo de dados que você inseriu.')
except ZeroDivisionError:
    print('Houve um problema com denominador zero, use outro valor.')
except KeyboardInterrupt:
    print('O usuário não preencheu o dado requerido.')
except ConnectionError:
    print('O site não está acessível!')
except Exception as erro:
    print(f'O erro foi: {erro.__cause__}')
else:
    print(f'O resultado da divisão é {r}')
finally:
    print(f'É com satisfação que lhe desejamos uma boa semana :D')
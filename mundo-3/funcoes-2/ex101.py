from datetime import datetime

def voto(ano):
    if idade < 18:
        return 'NÃO VOTA'
    elif 65 > idade >= 18:
        return 'VOTO OBRIGATÓRIO'
    elif idade >= 65:
        return 'VOTO OPCIONAL'


print('-=' * 20)
ano = int(input('Ano de nascimento: '))
idade = datetime.now().year - ano

print(f'Com {idade} anos: {voto(ano)}')
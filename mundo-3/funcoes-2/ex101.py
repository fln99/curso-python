def voto(ano):
    from datetime import datetime
    idade = datetime.today().year - ano

    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'        
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'

# Programa Principal
print('-=' * 20)
ano = int(input('Ano de nascimento: '))
print(f'{voto(ano)}')
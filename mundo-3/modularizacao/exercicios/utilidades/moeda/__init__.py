def aumentar(valor, form=False, qtd=0.15):
    """
    -> Função que concede um aumento de 15% de um salário/valor.
    :param valor: valor do capital a ser aumentado
    :param form: opção para formato monetário
    :return: retorno do valor já com o aumento
    """
    if form:
        return moeda(valor + (valor * qtd))
    else:
        return valor + (valor * qtd)


def diminuir(valor, form=False, qtd=0.30):
    """
    -> Função que diminui o valor em 30%.
    :param valor: total a ser modificado
    :param form: opção para formato monetário
    :return: valor com 30% de diminuição
    """
    if form:
        return moeda(valor - (valor * qtd))
    else:   
        return valor - (valor * qtd)


def dobro(valor, form=False):
    """
    -> Função para dobrar o valor de um número.
    :param valor: número a ser dobrado
    :param form: opção para formato monetário
    :return: valor dobrado
    """
    if form:
        return moeda(valor * 2)
    else:
        return valor * 2


def metade(valor, form=False):
    """
    -> Função que dividirá o valor na metade.
    :param valor: valor a ser dividido
    :param form: opção para formato monetário
    :return: retorno do valor dividido
    """
    if form:
        return moeda(valor / 2)
    else:
        return valor / 2


def moeda(valor):
    """
    -> Função para converter monetariamente.
    :param valor: valor a ser convertido
    :return: retorna o valor convertido
    """
    return f'R${valor}'


def resumo(valor, aum, dim):
    """
    -> Função que resume toda modificação disponível.
    :param valor: valor a ser colocado para ver o resumo
    :param aum: variável para a quantidade de aumento do valor
    :param dim: quantidade da redução do valor
    """
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)

    print(f'Valor analisado: {moeda(valor)}')
    print(f'Dobro do valor: {dobro(valor, True)}')
    print(f'Metade do valor: {metade(valor, True)}')
    print(f'{aum}% de aumento: {aumentar(valor, True, aum / 100)}')
    print(f'{dim}% de redução {diminuir(valor, True, dim / 100)}')
    print('-' * 30)
def notas(* notes, sit=False):
    """
    Esta função lhe permite criar um dicionário com o aproveitamento de um aluno.
    Há a possibilidade também de você realizar cálculo de média.
    OBS: A média é 6 e caso necessite alterar, entre em contato.

    :param notes: Notas a serem inseridas para o cálculo.
    :param sit: Ativa a amostragem da situação do aluno/pessoa.
    """
    boletim = dict()
    boletim['total'] = len(notes)
    boletim['maior'] = max(notes)
    boletim['menor'] = min(notes)
    boletim['média'] = sum(notes) / len(notes)
    if sit:
        if boletim['média'] >= 8:
            boletim['situação'] = 'BOA'
        elif boletim['média'] >= 6:
            boletim['situação'] = 'RAZOÁVEL'
        else:
            boletim['situação'] = 'RUIM'

    return boletim

# Programa Principal
resp = notas(2, 5, 10, 10, sit=True)
print(resp)
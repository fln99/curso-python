from utilidades import moeda

valor = int(input('Insira um número: '))

print(f'O aumento de {moeda.moeda(valor)} em 15% é igual a {moeda.aumentar(valor, True)}')
print(f'A diminuição de 30% em {moeda.moeda(valor)} resulta em {moeda.diminuir(valor, True)}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, True)}')
print(f'A metade de {moeda.moeda(valor)} é igual a {moeda.metade(valor, True)}')
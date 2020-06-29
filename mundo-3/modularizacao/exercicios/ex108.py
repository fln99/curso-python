from utilidades import moeda

valor = int(input('Insira um número: '))

print(f'O aumento de {moeda.moeda(valor)} em 15% é igual a {moeda.moeda(moeda.aumentar(valor))}')
print(f'A diminuição de 30% em {moeda.moeda(valor)} resulta em {moeda.moeda(moeda.diminuir(valor))}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'A metado de {moeda.moeda(valor)} é igual a {moeda.moeda(moeda.metade(valor))}')
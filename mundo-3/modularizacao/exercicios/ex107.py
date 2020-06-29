from utilidades import moeda

valor = int(input('Insira um número: '))

print(f'O aumento de {valor} em 15% é igual a {moeda.aumentar(valor)}')
print(f'A diminuição de 30% em {valor} resulta em {moeda.diminuir(valor)}')
print(f'O dobro de {valor} é {moeda.dobro(valor)}')
print(f'A metado de {valor} é igual a {moeda.metade(valor)}')
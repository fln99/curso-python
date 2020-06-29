from utilidades import moeda
from utilidades import dados

p = dados.leia_dinheiro('Insira um número: ')
moeda.resumo(p, 20, 10)
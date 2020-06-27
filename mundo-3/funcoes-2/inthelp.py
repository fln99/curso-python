# def teste(b):
#     global a
#     a = 8
#     b += 2
#     c = 2
#     print(f'A variável a na função vale {a}')
#     print(f'A variável b na função vale {b}')
#     print(f'A variável c na função vale {c}')


# a = 10
# teste(a)
# print(f'A variável a vale {a}')
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(10, 2)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Os valores das somas foram {r1}, {r2} e {r3}')
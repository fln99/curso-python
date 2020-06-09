p_termo = int(input('Primeiro termo da P.A: '))
raz_pa = int(input('Razão da sua P.A: '))

decimo = p_termo + (10 - 1) * raz_pa

for i in range(p_termo, decimo + raz_pa, raz_pa):
    print(i)
print('Finish')

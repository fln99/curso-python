p_termo = int(input('Primeiro termo da P.A: '))
raz_pa = int(input('Razão da sua P.A: '))

progress = []

for i in range(p_termo, len(10), raz_pa):
    print(p_termo + raz_pa)

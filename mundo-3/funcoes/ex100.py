from random import randint
numeros = []
pares = []

def sorteia():
    for i in range(0, 5):
        numeros.append(randint(0, 60))


sorteia()
def soma_par(lis):
    for num in lis:
        if num % 2 == 0:
            pares.append(num)


soma_par(numeros)

print(numeros)
print(f'A soma dos números pares da lista é {sum(pares)}')
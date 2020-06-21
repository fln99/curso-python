# teste = list()
# teste.append('Felipe')
# teste.append(20)

# galera = list()
# galera.append(teste[:])
# teste[0] = 'João'
# teste[1] = 30
# galera.append(teste[:])
# print(galera)

galera = [['João', 32], ['Maria', 10], ['Jubileu', 20], ['Bruna', 40]]

# print(galera[0][0])
# print(galera[1][1])

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade!')
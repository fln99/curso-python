# pessoas = {'nome': 'Felipe', 'sexo': 'M', 'idade': 20}
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())
# pessoas['nome'] = 'Jubileu' 
# pessoas['peso'] = 81
# for k, v in pessoas.items():
#     print(k, v)

estado = dict()
brasil = list()

for i in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
lado_a = int(input('Aresta A do triângulo: '))
lado_b = int(input('Aresta B do triângulo: '))
lado_c = int(input('Aresta C do triângulo: '))

if lado_a < lado_b + lado_c and lado_b < lado_a + lado_c and lado_c < lado_a + lado_b:
    print('De acordo com os lados inseridos, será possível a criação de um triângulo!')
else:
    print('Infelizmente não será possível criar um triângulo.')
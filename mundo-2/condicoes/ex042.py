lado_a = int(input('Aresta A do triângulo: '))
lado_b = int(input('Aresta B do triângulo: '))
lado_c = int(input('Aresta C do triângulo: '))

if lado_a < lado_b + lado_c and lado_b < lado_a + lado_c and lado_c < lado_a + lado_b:
    if lado_a == lado_b or lado_b == lado_a or lado_c == lado_a:
        print('O triângulo formado é do tipo Isósceles.')
    elif lado_a == lado_b and lado_a == lado_c and lado_b == lado_a and
else:
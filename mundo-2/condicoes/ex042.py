lado_a = int(input('Aresta A do triângulo: '))
lado_b = int(input('Aresta B do triângulo: '))
lado_c = int(input('Aresta C do triângulo: '))

if lado_a < lado_b + lado_c and lado_b < lado_a + lado_c and lado_c < lado_a + lado_b:
    if lado_a == lado_b and lado_b == lado_c:
        print('Seu triângulo é Equilátero')
    elif lado_a == lado_b or lado_b == lado_c:
        print('Seu triângulo é Isósceles')
    else:
        print('O triângulo formado é Escaleno!')
else:
    print('Não é possível formar triângulo com as medidas informadas!')
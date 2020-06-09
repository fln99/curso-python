lado_a = int(input('Aresta A do triângulo: '))
lado_b = int(input('Aresta B do triângulo: '))
lado_c = int(input('Aresta C do triângulo: '))

if lado_a < lado_b + lado_c and lado_b < lado_a + lado_c and lado_c < lado_a + lado_b:
    if lado_a == lado_b == lado_c:
        print('Seu triângulo é Equilátero')
    elif lado_a != lado_b != lado_c != lado_a:
        print('Seu triângulo é Escaleno')
    else:
        print('O triângulo formado é Isósceles!')
else:
    print('Não é possível formar triângulo com as medidas informadas!')
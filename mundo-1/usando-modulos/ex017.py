from math import hypot

cat_op = int(input('Medida do cateto oposto: '))
cat_ad = int(input('Medida do cateto adjacente: '))

print('O comprimento da hipotenusa será de {:.2f}px'.format(hypot(cat_op, cat_ad)))
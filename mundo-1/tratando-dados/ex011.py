width = float(input('Largura da parede = '))
heigth = float(input('Altura da parede = '))

area = width * heigth
paint_can = area / 2

print('Sua parede tem {} metros quadrados.'.format(area))
print('Serao necessarios {} litros de tinta!'.format(paint_can))
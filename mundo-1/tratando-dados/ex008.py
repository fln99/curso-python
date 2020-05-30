measure = float(input('Quantos metros deseja converter? '))

cent = measure * 100
mili = measure * 1000

print('{:.2f} metros contém'.format(measure), end=' -> ')
print('{:.2f} centímetros e {:.2f} milímetros!'.format(cent, mili))
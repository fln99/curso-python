my_dogs = ('Luke', 'Betove', 'Nik', 'Donizetti', 'Raposa')
age_dogs = (3, 7, 0.8, 6, 2)

for pos, dog in enumerate(my_dogs):
    print(f'Tenho um dog chamado {dog} e ele tem {age_dogs[pos]} anos!')

total = 0

for age in range(0, len(age_dogs)):
    total += age_dogs[age]

print(f'A média de idade de todos os meus cães é {total / len(age_dogs):.2f}')

print(sorted(my_dogs))
print(sorted(age_dogs))

print(my_dogs.index('Nik', 1))

print(my_dogs.count('Luke'))
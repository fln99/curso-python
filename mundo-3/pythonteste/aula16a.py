numbers = (1, 2, 5, 7, 1, 0, 10, 20, 30)

pair_total = 0

for num in sorted(numbers):
    if num % 2 == 0:
        print(num)
        pair_total += 1

print(f'Total de pares: {pair_total}')
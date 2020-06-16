import random

random_num = random.sample(range(11), 4)
random_tuple = (random_num[0], random_num[1], random_num[2], random_num[3])

print(f'A lista gerada foi: {random_tuple}')
print(f'O maior número é: {max(random_tuple)}')
print(f'O menor número é: {min(random_tuple)}')
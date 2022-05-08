import random

n = random.randint(1, 100)

x = random.choices(range(1, 10**3), k = n)

print(n)
print(*x)


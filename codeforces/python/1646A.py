import math

t = int(input())

for i in range(t):
    n, s = map(int, input().split())
    print(math.floor(s/(n**2)))

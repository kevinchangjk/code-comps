from collections import Counter

t = int(input())

def calc(x):
    return x*(x-1) // 2

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ain = [a[j]-j for j in range(n)]
    count = Counter(ain)
    res = sum(list(map(calc, list(count.values()))))
    print(res)
    
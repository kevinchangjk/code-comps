t = int(input())

def reversort(l, n):
    res = []
    cost = 0
    for i in range(n-1):
        cost += l.index(min(l)) + 1
        l[:l.index(min(l))+1] = l[l.index(min(l))::-1]
        res.append(l.pop(0))
    return cost

for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    print(f"Case #{i+1}: {reversort(l, n)}")
    
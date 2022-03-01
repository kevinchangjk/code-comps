t = int(input())

for i in range(t):
    n = int(input())
    h = list(map(int, input().split()))
    even = []
    odd = []
    
    for hh in h:
        if hh%2 == 0:
            even.append(hh)
        else:
            odd.append(hh)
    res = odd.copy()
    res.extend(even)
    print(*res)
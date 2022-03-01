t = int(input())
res = []

for i in range(t):
    n, W = list(map(int, input().split()))
    w = list(map(int, input().split()))
    
    w = sorted(w)[::-1]
    h = 1
    j = 1
    while len(w) > 1:
        if w[0] + w[j] <= W:
            w[0] += w.pop(j)
            j -= 1
        else:
            if j < len(w) - 1:
                j += 1
            else:
                w.pop(0)
                h += 1
                j = 1
    res.append(h)

print(*res)
    
n = int(input())
res = []

for t in range(n):
    r, g, b = list(map(int, input().split()))
    total = sum([r, g, b])
    if total == 0:
        res.append("NO")
        continue
    mx = max(r, g, b)
    if total%2 == 0:
        if mx >= (total//2 + 1):
            res.append("NO")
        else:
            res.append("YES")
    elif mx >= (total//2 + 2):
        res.append("NO")
    else:
        res.append("YES")
        
print("\n".join(res))
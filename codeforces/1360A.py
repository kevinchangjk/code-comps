t = int(input())
res = []

for i in range(t):
    a, b = list(map(int, input().split()))
    l = max(a,b)
    w = min(a,b)
    df = max(2*w, l)
    res.append(str(df**2))
    
print("\n".join(res))
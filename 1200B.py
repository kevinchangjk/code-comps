trials = int(input())
res = []

for i in range(trials):
    
    n, m, k = list(map(int, input().split()))
    h = list(map(int, input().split()))
    r = True
    
    for i in range(n-1):
        extra = m + h[i] - (h[i+1] - k)
        if extra < 0 :
            r = False
            break
        else:
            m = extra
    
    if r == True:
        res.append("YES")
    else:
        res.append("NO")
    
print("\n".join(res))
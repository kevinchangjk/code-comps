from collections import Counter

t = int(input())
res = []

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    acount = Counter(a)
    if max(acount.values()) > (n // 2):
        superm = max(acount.values())
        diff = 2 * superm - n
        res.append(diff)
        
    else:
        if n % 2 == 0:
            res.append(0)
        else:
            res.append(1)
            
print(*res)
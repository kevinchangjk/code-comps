from itertools import combinations

t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if max(a) - min(a) > max(a):
        print("NO")
    
    else:
        pairs = list(combinations(a, 2))
        dinit= [abs(p1-p2) for p1, p2 in pairs]
        dp = min(dinit)
        tt = min(min(a), dp)
        while tt < max(a):
            if tt not in a:
                a.append(tt)
            tt += dp
        if len(a) <= 300:
            print("YES")
            print(len(a))
            print(*a)
        else:
            print("NO")
            
            
    
    
    
    
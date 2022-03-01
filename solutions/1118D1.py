nm = input().split()
n = int(nm[0])
m = int(nm[1])
a = list(map(int, input().split()))

def solve(n, m, a):
    if max(a) > m:
        return 1
    if sum(a) < m:
        return -1
    
    waste = sum(a) - m
    
    d = 0
    while m > 0:
        k = 1
        target = max(a)
        a.remove(target)
        m -= target
        if len(a) > 0:
            target = max(a)
            
        while (target - k) > 0 and (waste - k) >= 0 and m > 0:
            target = max(a)
            a.remove(target)
            m -= (target-k)
            waste -= k
            k+=1
    
        d +=1
    return d

print(solve(n,m,a))
    
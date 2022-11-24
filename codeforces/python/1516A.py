t = int(input())

for i in range(t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    kk = k
    j = 0
    
    while k > 0 and j<(n-1):
        delt = min(a[j], k)
        a[j] -= delt
        k -= delt
        j += 1
    
    kk -= k
    
    a[n-1] += kk
        
    print(*a)
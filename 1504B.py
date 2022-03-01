t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input()))
    b = list(map(int, input()))
    
    if sum(a) != sum(b):
        print("NO")
    else:
        leg = [j for j in range(1, n+1, 2) if sum(a[:j+1]) == (j+1)//2]
        c = [abs(a[h]-b[h]) for h in range(n)]
        k = 0
        onz = 0
        req = []
        while k < n:
            if c[k] == 1 and k == n-1:
                req.append(k)
                k += 1
            elif c[k] == 1:
                onz = 1
                k += 1
            elif c[k] == 0 and onz == 1:
                req.append(k-1)
                k += 1
                onz = 0
            else: 
                k += 1
        solva = 1
        for requ in req:
            if requ in leg:
                continue
            else:
                print("NO")
                solva = 0
                break
        if solva == 1: 
            print("YES")
            
            
        
t = int(input())

for i in range(t):
    n = int(input())
    q = list(map(int, input().split()))
    qs = []
    
    for j in range(n):
        if j == 0:
            qs.append(q[j])
        else:
            if q[j] == q[j-1]:
                qs.append(0)
            else:
                qs.append(q[j])
    
    nmin = list(range(1, n+1))
    nmax = nmin.copy()
    
    minq = []
    maxq = []

    for thing in qs:
        if thing != 0:
            
            nmin.remove(thing)
            nmax.remove(thing)

    for k in range(n):
        if qs[k] != 0:
            minq.append(qs[k])
        else:
            minq.append(nmin.pop(0))

    for k in range(n):
        if qs[k] != 0:
            maxq.append(qs[k])
        else:
            maxq.append(nmax.pop(-1))
    
    print(*minq)
    print(*maxq)

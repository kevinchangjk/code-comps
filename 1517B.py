t = int(input())

for i in range(t):
    n, m = list(map(int, input().split()))
    mp = []
    res = [[0 for k in range(m)] for j in range(n)]
    for j in range(n):
        mp.append(list(map(int, input().split())))
    
    for k in range(m):
        minmp = [min(mpp) for mpp in mp]
        kind = minmp.index(min(minmp))
        for kk in range(n):
            if kk == kind:
                res[kk][k] = min(mp[kk])
                mp[kk].remove(min(mp[kk]))
            else:
                res[kk][k] = max(mp[kk])    
                mp[kk].remove(max(mp[kk]))
        
    [print(*ress) for ress in res]
        
    
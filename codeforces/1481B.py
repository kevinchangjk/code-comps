t = int(input())

for i in range(t):
    n, k = list(map(int, input().split()))
    h = list(map(int, input().split()))
    h_rev = h[::-1]
    hh = [h_rev[0]]
    '''
    hh = [h[i+1] - h[i] if h[i+1] > h[i] else 0 for i in range(n-1)]
    req = sum(hh)
    if k >= req:
        print(-1)
        
    else:
        for i in range(n-1):
            k-=hh[i]
            if k <= 0:
                print(i+1)
                break
'''

    for i in range(1, n):
        hh.append(max(hh[i-1], h_rev[i]))
        
    hh_rev = hh[::-1]
    diff = [hh_rev[i]-h[i] for i in range(n)]
    
    req = sum(diff)
    
    if k > req:
        print(-1)
        
    else:
        for i in range(n):
            k-=diff[i]
            if k <= 0:
                print(i)
                break
            
    
            
        
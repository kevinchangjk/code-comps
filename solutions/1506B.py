t = int(input())
res = []

for i in range(t):
    n, k = list(map(int, input().split()))
    s = input()

    s_indexed = [j for j, x in enumerate(s) if x == "*"]
    if len(s_indexed) == 1:
        res.append(1)
        
    else: 
        s_dist = [s_indexed[h]-s_indexed[h-1] for h in range(1, len(s_indexed))]
        s_count = []
        
        while len(s_dist) > 1:
            if s_dist[1] + s_dist[0] <= k:
                s_dist[0] += s_dist.pop(1)
                
            else:
                s_count.append(s_dist.pop(0))
                
        s_count.append(s_dist[0])
        res.append(len(s_count)+1)
    
print(*res)
    
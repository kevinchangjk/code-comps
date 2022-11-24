from collections import Counter

n = int(input())
cs = list(map(int, input().split()))
acs = list(map(int, input().split()))
guys = [(cs[i], acs[i]) for in range(n)]

clowns = 0
acrobats = 0
both = 0

count = Counter(guys)
if count[(1, 0)] == count[(0, 1)]:
    if count[(1, 1)] % 2 == 0:
        
    else:
        print(-1)
    
else:
    
        
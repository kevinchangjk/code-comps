n = int(input())
ts = list(map(int, input().split()))
counts = []
count = 0
counting = 0

for i in range(n):
    t = ts[i]
    if count == 0:
        count +=1
        counting = t
    elif t == counting:
        count +=1
    else: 
        counts.append(count)
        count = 1
        counting = t
    if i == n-1:
        counts.append(count)

streaks = [min(counts[i], counts[i+1]) for i in range(len(counts)-1)]
        
print(max(streaks)*2)
        

        
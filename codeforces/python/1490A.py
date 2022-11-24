import math

t = int(input())

def counts(ind):
    cons = [a[ind], a[ind-1]]
    divi = max(cons) / min(cons)
    return math.ceil(math.log(divi, 2))-1

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    countss = [counts(j) for j in range(1, n)]
    print(sum(countss))
    
    
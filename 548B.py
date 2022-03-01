n = int(input())
a = list(map(int, input().split()))

res = [a.pop()]

for ai in a[::-1]:
    if ai < res[-1]:
        res.append(ai)
    else:
        res.append(max(res[-1] -1, 0))
    
print(sum(res))
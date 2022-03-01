n = int(input())

a = list(map(int, input().split()))

streak = [1]
stree = 1
maxi = 1

for i in range(1, n):
    if a[i] >= a[i-1]:
        stree += 1
    else:
        stree = 1
    streak[i] = stree
    
    if stree > maxi:
        maxi = stree
        
print(maxi)
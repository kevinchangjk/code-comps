t = int(input())
res = []

for i in range(t):
    
    a = input()
    b = input()
    maxlen = 0
    
    for j in range(len(a)):
        tryi = 1
        dist = 1
        while j+dist <= len(a):
            if a[j:j+dist] in b:
                maxlen = max(maxlen, dist)
                dist += 1
                
            else:
                break
                
    res.append(len(a) + len(b) - 2 * maxlen)
    
print(*res)
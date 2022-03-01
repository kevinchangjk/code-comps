  
from collections import Counter

n = int(input())
a = list(map(int, input().split()))

count = Counter(a)

def doub(key):
    if count[key] == 2:
        doubled.append(key)
    return

if max(count.values()) <= 2:
    doubled = []
    irr = list(map(doub, count.keys()))
    desc = list(map(str, sorted(doubled, reverse = True)))
    asc = list(map(str, sorted(count.keys())))
    
    print("YES")
    print(len(asc))
    print(" ".join(asc))
    print(len(desc))
    print(" ".join(desc))
    
else:
    print("NO")
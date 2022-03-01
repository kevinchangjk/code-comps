from collections import Counter

nk = list(map(int, input().split()))
n, k = nk[0], nk[1]

s = list(map(int, input().split()))
count = Counter(s)

if len(count) == 1:
    print(count.keys()[0]+)
elif len(count) 
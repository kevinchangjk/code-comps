from collections import Counter

t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a_aug = sorted(a)
    count = Counter(a_aug)
    res = -1
    for ai in count:
        if count[ai] == 1:
            res = a.index(ai) + 1
            break
        else:
            continue
    print(res)
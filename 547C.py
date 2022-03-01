from collections import Counter

n = int(input())
qi = list(map(int, input().split()))

qi_sum = [0]
for q in qi:
    qi_sum.append(q+qi_sum[-1])

if 1 in qi_sum:
    a = n - max(qi_sum)
    if min(qi_sum) + a ==1:
        pi = [a + q for q in qi_sum]
        count = Counter(pi)
        if len(count) == n:
            print(" ".join(list(map(str, pi))))
        else:
            print(-1)
    else:
        print(-1)
else:
    a = n
    if min(qi_sum) + a ==1:
        pi = [a + q for q in qi_sum]
        count = Counter(pi)
        if len(count) == n:
            print(" ".join(list(map(str, pi))))
        else:
            print(-1)
    else:
        print(-1)
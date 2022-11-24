from collections import Counter

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def res(i):
    if b[i] == a[i] == 0:
        return 'a'
    if a[i] == 0:
        return 'n'
    return -b[i] / a[i]

di = list(map(res, range(n)))

count = Counter(di)
if 'n' in count:
    count.pop('n')

if 'a' in count:
    ret = count['a']
    count.pop('a')

else:
    ret = 0

if len(count) > 0:
    print(max(count.values()) + ret)

else:
    print(0 + ret)
from collections import Counter

nk = list(map(int, input().split()))
n, k = nk[0], nk[1]
di = list(map(lambda x: int(x)%k, input().split()))
count = Counter(di)

for i in range(k):
    if i not in count:
        count.update({i: 0})

gifts = count[0] //2

if k % 2 == 0:
    gifts += count[k//2]//2
    gifts += sum(map(lambda i: min(count[i], count[k-i]), range(1, k//2)))

else:
    gifts += sum(map(lambda i: min(count[i], count[k-i]), range(1, k//2 + 1)))

print(gifts*2)
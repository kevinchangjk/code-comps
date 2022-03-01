t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    tai = a.index(max(a))
    tbi = a.index(min(a))
    da = min(tai, tbi) + 1
    db = n - max(tai, tbi)
    dc = abs(tai-tbi)
    print(sum([da, db, dc])-max([da, db, dc]))
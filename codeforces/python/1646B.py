def checker(a, n):
    divider = n //2 + 1
    bsum = a[0]
    rsum = 0
    blist = a[1:divider]
    rlist = a[-1:divider-1:-1]
    while len(blist) > 0 and len(rlist) > 0:
        rsum += rlist.pop(0)
        bsum += blist.pop(0)
        if rsum > bsum:
            return True
    return False

t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if checker(a, n):
        print("YES")
    else:
        print("NO")

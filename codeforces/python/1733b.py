t: int = int(input())


def solve():
    n, x, y = map(int, input().split())
    if x != 0 and y != 0:
        print(-1)
        return

    eff = x + y
    if eff == 0 or (n - 1) % eff != 0:
        print(-1)
        return
    
    res = []
    for i in range((n - 1) // eff):
        curr = 2 + i * eff
        res += [curr for j in range(eff)]
    
    print(*res)
    return


for _ in range(t):
    solve()

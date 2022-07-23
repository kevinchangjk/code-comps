t = int(input())

def solve(n, a):
    first = a[0]

    for i in range(1, n):
        if a[i] % first != 0:
            return "NO"
        else:
            continue
    return "YES"

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    print(solve(n, a))

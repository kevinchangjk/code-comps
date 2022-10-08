def solve(a, b, c):
    d = a & b
    x = 0
    shamt = 0
    while d | c > 0:
        masked_d = d & 1
        masked_c = c & 1
        if masked_d ^ masked_c != 0:
            if masked_d == 0:
                x += 1 << shamt
            else:
                return -1
        shamt += 1
        d >>= 1
        c >>= 1
    return x


t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    print(solve(a, b, c))

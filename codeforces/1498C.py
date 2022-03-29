t = int(input())
pmod = (10**9 + 7)

def scalc(nk):
    n, k = nk
    if k == 1:
        return 1
    elif n == 1:
        return 2
    if k == 2:
        return n+1
    else:
        s = [n+1]
        ss = list(range(n-1, 0, -1))
        for i in range(k-3):
            s.append(sum(ss))
            ss = [sum(ss[:j]) % pmod for j in range(n-1, 0, -1)]
        s.append(sum(ss))
        return sum(s) % pmod

nk = [list(map(int, input().split())) for i in range(t)]

res = [scalc(nnkk) for nnkk in nk]

print(*res)
    
t = int(input())
res = []

for test in range(t):
    n, s = list(map(int, input().split()))
    a = list(map(int, input().split()))
    asum = [sum(a[:i]) for i in range(1, len(a)+1)]
    
    if asum[-1] <= s:
        result = 0
    elif asum[-1] >= s:
        asummex = [asum[i] > s for i in range(len(asum))]
        apex = asummex.index(1)
        mx = max(a[:apex])
        if mx > a[apex]:
            result = a.index(mx) + 1
    res.append(str(result))
    
print("\n".join(res))
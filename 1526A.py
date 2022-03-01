t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ass = sorted(a)
    res = [ass[j//2] if j%2==0 else ass[-((j//2)+1)] for j in range(2*n)]
    print(*res)
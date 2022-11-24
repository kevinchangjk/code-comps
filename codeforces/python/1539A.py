t = int(input())

for i in range(t):
    n, x, t = list(map(int, input().split()))
    dis = int(t/x)
    summa = dis*(dis+1)//2
    total = n*dis-summa
    print(total)
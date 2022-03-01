t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    avg = sum(a)/n
    if int(avg)-avg != 0:
        print(-1)
    else:
        totl = [1 for aa in a if aa > avg]
        print(sum(totl))
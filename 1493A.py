T = int(input())

for i in range(T): 
    n, k = list(map(int, input().split()))
    res = [str(i) for i in range(1,n+1) if (i >= k / 2) and (i != k)]
    amount = len(res)
    if amount == 0:
        print(0)
    else: 
        print(amount)
        print(" ".join(res))
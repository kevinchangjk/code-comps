t = int(input())

for i in range(t):
    nlen, mlen = list(map(int, input().split()))
    n = list(map(int, input().split()))
    m = list(map(int, input().split()))
    cancel = 0
    for train in n:
        if train in m:
            cancel +=1
    print(cancel)
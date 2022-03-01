t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if sum(a) < n:
        print(1)
    else:
        print(sum(a)-n)
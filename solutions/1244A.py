t = int(input())

for i in range(t):
    a, b, c, d, k = list(map(int, input().split()))
    if a%c !=0:
        x = a//c + 1
    else:
        x = a//c
    if b%d !=0:
        y = b//d +1
    else:
        y = b//d

    if x+y>k:
        print(-1)
    else:
        print(f"{x} {y}")
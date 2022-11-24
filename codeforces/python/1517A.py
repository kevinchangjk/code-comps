import math

t = int(input())

for i in range(t):
    n = int(input())
    count = 0
    solve = 1
    while n > 0:
        if n >= 2050:
            deg = int(math.log10(n))-3
            div = 2050 * 10**deg
            if n >= div:
                pass
            else:
                div = div // 10
                
            countt = n // div
            n -= countt*div
            count += countt
        else:
            solve = 0
            break
    
    if solve == 0:
        print(-1)
    else:
        print(count)
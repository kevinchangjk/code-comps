# Grasshopper Codeforces 1607B

t = int(input())

for _ in range(t):
    pos, n = map(int, input().split())
    even = pos%2 == 0

    i = 1
    count = 0
    if even:
        while n > 0 and count != 3:
            if pos%2 == 0:
                pos -= i
            else:
                pos += i
            n -= 1
            i += 1
            count += 1
            
    else:
        while n > 0 and count != 1:
            pos += i
            n -= 1
            i += 1
            count += 1

    rem = n%4
    pos += (n-rem)
    i += n-rem
    n = rem

    while n>0:
        if pos%2 == 0:
            pos -= i
        else:
            pos += i
        n -= 1
        i += 1
        
    print(pos)

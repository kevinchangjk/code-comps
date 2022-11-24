t = int(input())

for i in range(t):
    n = int(input())
    
    if n == 1:
        print(1)
    elif n == 2:
        print(-1)
    else:
        mat = []
        nn = n**2
        if n % 2 == 0:
            a, b = list(range(1, nn+1))[:(nn//2)], list(range(1, nn+1))[(nn//2):]
        else:
            a, b = list(range(1, nn+1))[:(nn//2 + 1)], list(range(1, nn+1))[nn//2 + 1:]
        for j in range(n):
            mat.append([a[(k+j*n)//2] if ((k+j*n) % 2==0) else (b[(k+j*n)//2]) \
                          for k in range(n)])
        for row in mat:
            print(*row)
    

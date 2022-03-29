nm = list(map(int, input().split()))
n, m = nm[0], nm[1]
count = 0
factor = m / n
if factor % 1 != 0:
    print(-1)
    
else:
    while factor % 2 == 0:
        factor//=2
        count +=1
    while factor%3 == 0:
        factor //=3
        count+=1
    if factor == 1:
        print(count)
    else:
        print(-1)
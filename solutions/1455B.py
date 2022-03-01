t = int(input())

for i in range(t):
    x = int(input())
    running = True
    k = 0
    d = 0
    while running:
        k+=1
        d +=k
        if d >= x:
            running = False
    if (d-x) < k and (d-x) > 1:
        print(k)
    else:
        print(k+(d-x))
    
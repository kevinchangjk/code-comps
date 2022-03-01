t = int(input())

for i in range(t):
    n = int(input())
    tm = input()
    mt = tm[::-1]
    t = 0
    m = 0
    tt = 0
    mm = 0
    fail = 0
    
    for j in range(n):
        if tm[j] == "T":
            t += 1
        else:
            m += 1
        if mt[j] == "T":
            tt += 1
        else:
            mm += 1
        if m > t or mm > tt:
            fail = 1
            break
    if t == 2 * m and fail == 0:
        print("YES")
    
    else:
        print("NO")
        
import math

t = int(input())
for i in range(t):
    n = int(input())
    base = int(math.log(n, 10)) * 9
    nn = str(n)
    nref = int(nn[0])
    for nnn in nn:
        if int(nnn) < nref:
            supp = nref - 1
            break
        elif int(nnn) > nref:
            supp = nref
            break
    else:
        supp = nref
    print(base + supp)
    
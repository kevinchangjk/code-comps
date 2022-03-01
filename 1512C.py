t = int(input())

for i in range(t):
    pal = 1
    a, b = list(map(int, input().split()))
    s = list(input())
    lens = len(s)
    if lens % 2 == 0:
        if a % 2 != 0 or b % 2 != 0:
            print(-1)
            pal = 0
            continue
        else:
            pass
    else:
        if a%2 == 1:
            odd = '0'
        else:
            odd = '1'
        if s[lens//2] == odd:
            pass
        elif s[lens//2] == '?':
            s[lens//2] = odd
            if odd == '0':
                a -= 1
            else:
                b -= 1
        else:
            print(-1)
            pal = 0
            continue
    pnts = []
    for j in range(lens//2):
        x, y = s[j], s[-j-1]
        xy = {x, y}
        if xy == {'0', '1'}:
            print(-1)
            pal = 0
            break
        elif '?' in xy and len(xy) == 2:
            xy.remove('?')
            xy = xy.pop()
            s[j], s[-j-1] = xy, xy
            if xy == '0':
                a -= 2
            else:
                b -= 2
        elif len(xy) == 1 and '?' not in xy:
            xy = xy.pop()
            if xy == '0':
                a -= 2
            else:
                b -= 2
            continue
        else:
            pnts.append(j)
    for pnt in pnts:
        if a > 0:
            outs = '0'
            a -= 2
        else:
            outs = '1'
            b -= 2
        s[pnt], s[-pnt-1] = outs, outs
    if pal == 1:
        print("".join(s))
        
        
        
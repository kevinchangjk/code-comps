from collections import Counter

t = int(input())

for i in range(t):
    n, m = list(map(int, input().split()))
    a = input().split()
    b = input().split()
    need = b.copy()
    c = input().split()
    res = 'YES'
    
    if c[-1] not in b:
        res = 'NO'
    else:
        for i in range(n-1, -1, -1):
            if a[i] == b[i]:
                need.pop(i)
        needc = Counter(need)
        cc = Counter(c)
        for colour in needc:
            if needc[colour] <= cc[colour]:
                continue
            else:
                res = 'NO'
                break
        if res != "NO":
            order = []
            spare = b.index(c[-1])
            for i in range(m):
                if c[i] in need:
                    index = b.index(c[i])
                    order.append(str(index+1))
                    b[index] = 0
                else: 
                    order.append(str(spare+1))
    if res == 'NO':
        print(res)
    else:
        print(res)
        print(" ".join(order))
        
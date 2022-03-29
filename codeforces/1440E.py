n, q = list(map(int, input().split()))

a = list(map(int, input().split()))

for i in range(q):
    t, x, y = list(map(int, input().split()))
    if t == 1:
        b = [max([a[i], y]) for i in range(x)]
        b.extend(a[x:])
        a = b
    else:
        meals = 0
        for ai in a[x-1:]:
            if y >= ai:
                y -= ai
                meals +=1
        print(meals)
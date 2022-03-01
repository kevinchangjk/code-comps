n, k = list(map(int, input().split()))
t = []
b = []


def song_add(song):
    ti, bi = list(map(int, input().split()))
    t.append(ti)
    b.append(bi)
    return

irrelevant = list(map(song_add, range(n)))
maxi = 0

for ki in range(1, k+1):
    targets = sorted(b)[:ki]
    time = sum(map(lambda x: t[b.index(x)], targets))
    res = time * targets[-1]
    if res >= maxi:
        maxi = res
    else:
        break
    
print(maxi)
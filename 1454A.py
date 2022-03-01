t = int(input())

for i in range(t):
    n = int(input())
    res = [j+1 for j in range(n)]
    res.pop(0)
    res.append(1)
    print(" ".join(map(str, res)))
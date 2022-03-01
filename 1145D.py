n = int(input())
a = list(map(int, input().split()))

x = a[2]
y = min(a)

x2 = list(bin(x)[2:])
y2 = list(bin(y)[2:])

if len(y2) > len(x2):
    for i in range(len(y2) - len(x2)):
        x2.insert(0, '0')

if len(x2) > len(y2):
    for i in range(len(x2) - len(y2)):
        y2.insert(0, '0')

res = []

for i in range(len(x2)):
    if sum(list(map(int, [x2[i], y2[i]]))) == 1:
        res.append("1")
    else:
        res.append("0")
        
res = int("".join(res), 2) + 2

print(res)

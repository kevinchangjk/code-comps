n = int(input())
b = input().split(" ")

delta = [0]
for i in range(n):
    delta.append(delta[-1] + int(b[i])*((-1)**i))

def testss(i):
    if i >0:
        if b[i] == b[i-1]:
            return res[-1]
    delta1 = delta[i]
    delta2 = delta[-1] - delta[i+1]
    if delta2 == delta1:
        return 1
    return 0

res = []
for i in range(n):
    res.append(testss(i))
print(sum(res))
q = int(input())
inputs = []
for i in range(q):
    inputs.append(input())

def solve(q):
    q = q.split(" ")
    n = int(q[0])
    a = int(q[1])
    b = int(q[2])
    res = 0
    if b/2 <a:
        res += (n//2) * b
        res += (n % 2) * a
    else:
        res += n*a
    return res

for i in inputs:
    print(solve(i))
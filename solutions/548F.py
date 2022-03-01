n, m = list(map(int, input().split()))
p = list(map(int, input().split()))
s = list(map(int, input().split()))
b = list(map(int, input().split()))
y = list(map(int, input().split()))
pf = list(map(int, input().split()))

def pick(person):
    dishes = list(filter(lambda x: x!= -1, [i if (p[i] <= y[person] <= s[i] and abs(b[i]-pf[person]) <= (y[person]-p[i])) else -1 for i in range(n)]))
    return len(dishes)

dishes = list(map(lambda x: str(pick(x)), range(m)))
print(" ".join(dishes))
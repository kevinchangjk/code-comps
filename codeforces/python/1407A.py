t = int(input())

def test(liss):
    lissa = liss[::2]
    lissb = liss[1::2]
    return sum(lissa) - sum(lissb)

def result(res):
    res = list(map(str, res))
    print(len(res))
    print(" ".join(res))
    return

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if test(a) == 0:
        result(a)
    elif 
    
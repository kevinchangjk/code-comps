from collections import Counter

n = int(input())

def dcalc(liss):
    act = []
    dd = 0
    for i in range(len(liss)):
        act.append(liss[i])
        d = max(act)-min(act)
        dd += d
    return dd

s = list(map(int, input().split()))
sc = Counter(s)
mode_n = max(sc.values())
mode = list(sc.keys())[list(sc.values()).index(mode_n)]

so = [mode for i in range(mode_n)]
s = [ss for ss in s if ss != mode]
mx = mode
mn = mode

def delta(x):
    if x > mx:
        return x-mx
    else:
        return mn-x

for i in range(len(s)):
    sa = [delta(ss) for ss in s]
    tgt = sa.index(min(sa))
    so.append(s.pop(tgt))
    
print(dcalc(so))
t = int(input())

def ops(n, nlen):
    if nlen == 2:
        return 0
    moves = [abs(n[j+1]-n[j]) for j in range(nlen-1)]
    moves_duo = [moves[k+1]+moves[k] for k in range(nlen-2)]
    point = moves_duo.index(max(moves_duo))
    diff = abs(n[point+2]-n[point])
    return sum(moves)-max(moves_duo)+diff

for i in range(t):
    nlen = int(input())
    n = list(map(int, input().split()))
    print(ops(n, nlen))
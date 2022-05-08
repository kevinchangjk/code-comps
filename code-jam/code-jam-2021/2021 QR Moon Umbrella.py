t = int(input())

for i in range(t):
    xys = list(input().split())
    x, y = list(map(int, xys[:2]))
    s = list(xys[2])
    cost = 0
    if s[0] == "?":
        for ss in s[1:]:
            if ss !="?":
                s[0] = ss
                break
    for j in range(0, len(s)-1):
        blk = s[j:j+2]
        if blk[1] == "?":
            s[j+1] = s[j]
        elif blk == ["C", "J"]:
            cost += x
        elif blk == ["J", "C"]:
            cost += y
    print(f"Case #{i+1}: {cost}")
        
from itertools import combinations

t = int(input())

def prod(liss):
    i = 0
    res = 1
    while i < len(liss):
        res *= liss[i]
        i += 1
    return res

for i in range(t):
    m = int(input())
    cards = []
    for j in range(m):
        p, n = list(map(int, input().split()))
        for k in range(n):
            cards.append(p)
    cards.sort()
    maxx = sum(cards)
    res = [0]
    
    for h in range(1, len(cards)):
        combi = list(combinations(cards, h))
        combi = [comb for comb in combi if prod(comb) < maxx]
        combi.reverse()
        if len(combi) == 0:
            break
        ii = 0
        trying = 1
        while ii < len(combi) and trying:
            cardss = cards.copy()
            product = 1
            for comb in combi[ii]:
                product *= cardss.pop(cardss.index(comb))
            if product == sum(cardss):
                res.append(product)
                trying = 0
            else:
                ii += 1
    result = max(res)
    print(f"Case #{i+1}: {result}")
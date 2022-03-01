t = int(input())

for i in range(t):
    n, c0, c1, h = list(map(int, input().split()))
    s = input()
    
    if c0 == c1:
        res = n * c0
        
    elif c0 > c1:
        if h + c1 < c0:
            res = n * c1 + sum([h for bina in s if bina == "0"])
        else:
            res = sum([c0 for bina in s if bina == "0"]) + \
            sum([c1 for bina in s if bina =="1"])
    
    else:
        if h + c0 < c1:
            res = n * c0 + sum([h for bina in s if bina == "1"])
        else:
            res = sum([c0 for bina in s if bina == "0"]) + \
            sum([c1 for bina in s if bina =="1"])
    print(res)
t = int(input())
results = []

for i in range(t):
    a, b, c, r = list(map(int, input().split()))
    start = min(a, b)
    end = max(a, b)
    c_l = c-r
    c_u = c+r
    if c_u <= start:
        res = end-start
        
    else:
        if c_l <= start:
            if c_u <= end:
                start = c_l
                res = end-start-2*r
            else:
                res = 0
        else:
            if c_u <= end:
                res = end-start-2*r
            else:
                if c_l <= end:
                    end = c_u
                    res = end-start-2*r
                else:
                    res = end-start
    results.append(str(res))
    
print("\n".join(results))


        


import math

t = int(input())

for i in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    count = 0
    for j in range(1, n):
        xi, xj = x[j-1], x[j]
        if xi < xj:
            continue
        elif xi == xj:
            count += 1
            x[j] *= 10
            continue
        else:
            diff = int(math.log10(xi)) - int(math.log10(xj))
            if int(str(xi)[0]) == int(str(xj)[0]):
                if str(xj) == str(xi+1)[:len(str(xj))] and diff > 0:
                    count += diff
                    x[j] = xi+1
                    continue
                else:
                    diff += 1
                    
            elif int(str(xi)[0]) < int(str(xj)[0]):
                pass
            
            else:
                diff += 1
            
            count += diff
            x[j] *= (10**(diff))
    
    print(f"Case #{i+1}: {count}")

    
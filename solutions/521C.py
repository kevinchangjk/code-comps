n = int(input())
ai = list(map(int, input().split()))
summa = sum(ai)

def solve(i):
    if (summa-ai[i])%2 !=0:
        return -1
    if int(summa-ai[i])/2 in ai:
        if summa == 3*ai[i]:
            return -1
        return str(i+1)
    return -1
    
nice = list(filter(lambda x: x !=-1, map(solve, range(n))))
print(len(nice))
if len(nice) > 0:
    print(" ".join(nice))
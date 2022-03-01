t = int(input())

def primef(x, k):
    factors = 1
    while x%2 == 0:
        x/=2
        factors += 1
        if factors>= k+1:
            return 0
    div = 3
    while div <= x**0.5:
        if x%div == 0:
            x/=div
            factors += 1
            if factors>= k+1:
                return 0
        else:
            div +=2
    if x !=1:
        factors += 1
        if factors>= k+1:
            return 0
    return factors

for i in range(t):
    a, b, k = list(map(int, input().split()))

    if k >= 2:
        ap = primef(a, k)
        if ap == 0:
            print("YES")
        else:
            k -= (ap-1)
            bp = primef(b, k)
            if bp == 0:
                print("YES")
            else:
                print("NO")
            
    else:
        if a != b:
            if max(a, b) % min(a, b) ==0:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    
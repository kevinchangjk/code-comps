t = int(input())

for i in range(t):
    r, b, d = list(map(int, input().split()))
    
    if d == 0:
        if r == b:
            print("YES")
        else:
            print("NO")
    else:
        
        if ((max(r, b)-min(r, b)) / d) <= min(r, b):
            print("YES")
        else:
            print("NO")
from collections import Counter

t = int(input())
for i in range(t):
    n, k = list(map(int, input().split()))
    a = sorted(input())
    b = sorted(input())
    a_min = min(Counter(a).values())
    b_min = min(Counter(b).values())
    if a == b: 
        print("YES")
    elif a > b:
        print("NO")
    else:
        if k <= min(a_min, b_min):
            print("YES")
        else:
            print("NO")
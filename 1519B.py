t = int(input())

for i in range(t):
    n, m, k = list(map(int, input().split()))
    
    if (n*m - 1) == k:
        print("YES")
    else:
        print("NO")
t = int(input())

for i in range(t):
    n, k = list(map(int, input().split()))
    h = list(map(int, input().split()))
    
    while k > 0:
        j = 1
        while h[j] <= h[j-1]:
            j += 1
            if j == n:
                print(-1)
                k = 0
                break
        k -= 1
        h[j-1] +=1
        
    if j != n:
        print(j)
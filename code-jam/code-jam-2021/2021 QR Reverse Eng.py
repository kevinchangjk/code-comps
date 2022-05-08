t = int(input())

def reverse_eng(n, c):
    if c > (n*(n+1)-2) / 2 or c < n-1:
        return "IMPOSSIBLE"
    
    l = list(range(1, n+1))
    j = 2
    while c > n-j+1:
        ll = min(c-n+j, j)
        if ll == j:
            l[-j:] = l[-j+ll-1:-j-1:-1]
        else: 
            l[-j:-j+ll] = l[-j+ll-1:-j-1:-1]
        c -= ll
        j+=1
    return " ".join(map(str, l))

for i in range(t):
    n, c = list(map(int, input().split()))
    print(f"Case #{i+1}: {reverse_eng(n, c)}")
    
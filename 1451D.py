t = int(input())

for i in range(t):
    d, k = list(map(int, input().split()))
    d = d / k
    half = d**2 / 2
    p = int(half**(0.5))
    
    if p**2 + (p+1)**2 <= d**2:
        q = p+1
    else:
        q = p
        
    if (q+p) % 2 == 0:
        print("Utkarsh")
    else:
        print("Ashish")
    
t = int(input())
results = []

for i in range(t):
    n, m = list(map(int, input().split()))
    count = 0
    for j in range(n):
        row = input()
        if row[-1] == 'R':
            count +=1
        if j == n-1:
            nm = row
    for direction in nm:
        if direction == 'D':
            count +=1
            
    results.append(str(count))
    
print("\n".join(results))
    
        
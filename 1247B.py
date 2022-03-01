t = int(input())
output = []

for testcase in range(t):
    n, k, d = list(map(int, input().split()))
    a = list(map(int, input().split()))
    results = []
    
    for i in range(n-d+1):
        tries = set([])
        case = a[i:i+d]
        arbitrary = [tries.add(case[j]) for j in range(d)]
        results.append(len(tries))
        
    output.append(str(min(results)))

print("\n".join(output))
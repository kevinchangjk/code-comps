t = int(input())
q = []

for i in range(t):
    query = list(map(int, input().split()))
    q.append(query)
    
def solve(query):
    a, b, k = query[0], query[1], query[2]
    if k %2 == 0:
        return str((k//2)*(a-b))
    else:
        return str((k//2)*(a-b) + a)
    
res = list(map(solve, q))
print("\n".join(res))
    
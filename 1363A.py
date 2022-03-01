t = int(input())
res = []

for i in range(t):
    n, x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    odd_count = sum(map(lambda j: j%2 == 1, a))
    if odd_count == 0:
        result = "No"
    elif odd_count == n and x%2 == 0:
        result = "No"
    elif x == n and odd_count % 2 == 0:
        result = "No"
    else:
        result = "Yes"
    res.append(result)
    
print("\n".join(res))
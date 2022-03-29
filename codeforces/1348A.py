t = int(input())
result = []

for i in range(t):
    n = int(input())
    
    numbers = [2**i for i in range(1, n+1)]
    a = numbers[-1] + sum(numbers[:((n//2)-1)])
    b = sum(numbers[((n//2)-1):(n-1)])
    res = abs(a-b)
    result.append(str(res))
    
print("\n".join(result))
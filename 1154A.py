n = list(map(int, input().split()))

maxi = max(n)

res = [str(maxi - num) for num in n]

res.remove('0')

print(" ".join(res))
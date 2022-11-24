x = list(map(int, input().split()))
print(x)
summ = max(x)
x.remove(summ)

res = [str(summ-xi) for xi in x]
print(" ".join(res))
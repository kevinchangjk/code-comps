import math

a, b = map(int, input().split())
res = math.log(b/a, 3/2)
if res%1 == 0:
    res = math.ceil(res+1)
else: 
    res = math.ceil(res)
print(res)

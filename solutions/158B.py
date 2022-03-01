from collections import Counter

n = int(input())

s = list(map(int, input().split()))
taxis = 0

count = Counter(s)
for i in range(1, 5):
    if i not in count:
        count[i] = 0

add = 0
taxis += count[4]
taxis += count[2] // 2
count[2] %=2
add += min(count[3], count[1])
taxis +=add
count[3] -=add
count[1] -=add
taxis += count[1] // 4
count[1] %= 4
if count[2] == 1:
    if count[1] >=2:
        taxis +=1
        count[2] = 0
        count[1] -=2
    elif count[1] == 1:
        taxis +=1
        count[1] = 0
        count[2] = 0
if count[1] >0:
    count[1] = 1

taxis += sum([count[1], count[2], count[3]])
print(taxis)
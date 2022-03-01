n = int(input())
ai = list(map(int, input().split()))
disturbed = []
k = 0

for i in range(1, n-1):
    if ai[i-1:i+2] == [1, 0, 1]:
        if i-2 in disturbed:
            disturbed[-1] = i-1
        else:
            disturbed.append(i)

if len(disturbed) == 0:
    print(0)

else:
    print(len(disturbed))
    
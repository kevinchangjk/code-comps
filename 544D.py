n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [0 for i in range(n)]
d = [(c[i]-b[i]) / a[i] if a[i] != 0 else 'Nope' for i in range(n)]

count = {}
for counting in d:
    if counting not in count.keys():
        count[counting] = 1
    else:
        count[counting] +=1

if 'Nope' in count:
    count.pop('Nope')

if len(count.values()) == 0:
    maxx = 0
    
else:
    maxx = max(count.values())

print(maxx)
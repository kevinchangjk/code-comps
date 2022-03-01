nk = list(map(int, input().split()))
n = nk[0]
k = nk[1]
d = list(map(int, input().split()))
candies = []
d = sorted(list(map(lambda x: x%k, d)))

count = {}

def indexing(i):
    if i in d:
        return d.index(i)
    return None

indices = []

for i in range(k):
    index = indexing(i)
    if index = None:
        continue
    indices.append(index)

count = [indices[i+1] - indices[i] if i<k-1 else n-indices[i] for i in range(k)]
    
gifts = count[0] // 2

if k % 2 ==0:
    i = 1
    while i < k/2:
        gifts += min([count[i], count[-i]])

for res in d:
    if res in candies:
        candies.remove(res)
        gifts +=1
    else:
        if res == 0:
            candies.append(0)
        else:
            candies.append(k-res)
                    
    
print(gifts*2)
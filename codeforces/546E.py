n = int(input())
a = list(map(int, input().split()))
k = list(map(int, input().split()))
q = int(input())

def add_update(ai):
    ind = a.index(ai)
    return max(ai, a[ind-1] + k[ind-1])

def add(i, x):
    a[i-1] += x
    for ai in a[i:]:
        ai = add_update(ai)
    return a

printed = []

for i in range(q):
    query = input().split()
    if query[0] == '+':
        a = add(int(query[1]), int(query[2]))
    elif query[0] == 's':
        printed.append(str(sum(a[int(query[1])-1:int(query[2])])))
        
print("\n".join(printed))
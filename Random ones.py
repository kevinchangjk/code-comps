
n = int(input())
res = 0
    
for i in range(n):
    statement = input()
    if "+" in statement:
        res +=1
    else:
        res -=1
    
print(res)







one = input()
two = input()
res = 0
base = 'abcdefghijklmnopqrstuvwxyz'

for i in range(len(one)):
    if one[i].lower() == two[i].lower():
        continue
    elif base.index(one[i].lower()) < base.index(two[i].lower()):
        res = -1
        break
    else:
        res = 1
        break

print(res)






post = list(map(int, input()))
post.append(0)

def thing(nu):
    for i in range(len(post)-6):
        if sum(post[i:i+7]) in [0, 7]:
            return "YES"
    return "NO"

print(thing(2))
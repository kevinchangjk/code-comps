t = int(input())
res = []

for i in range(t):
    s = input()
    count = 1
    s_rev = []
    for i in range(len(s)):
        if i == len(s)-1:
            s_rev.append(count)
        elif s[i] == s[i+1]:
            count +=1
        else:
            s_rev.append(count)
            count = 1
            
    fix = 0
    
    while len(s_rev) > 2:
        target = min(s_rev)
        index_t = s_rev.index(target)
        if index_t == 0:
            s_rev[index_t+1] += target
            s_rev.pop(0)
            fix +=target
            continue
        elif index_t == len(s_rev)-1:
            s_rev[index_t-1] += target
            s_rev.pop(index_t)
            fix +=target
            continue
        else:
            s_rev[index_t-1] += (target + s_rev[index_t+1])
            s_rev.pop(index_t)
            s_rev.pop(index_t)
            fix +=target
    res.append(str(fix))
    
print("\n".join(res))
    
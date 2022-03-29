n = int(input())
l = input()
r = input()
boots = []
available = r.copy()

for i in range(n):
    if l[i] == "?":
        ql +=1
        continue
    if l[i] in available:
        boot = l[i]
        index = r.index(boot)
        boots.append(i+" "+index)
        available.remove(boot)
    else:
            
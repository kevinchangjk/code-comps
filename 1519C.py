t = int(input())

def strengths(studs, k):
    slen = len(studs)
    if k == 1:
        return sum(studs)
    elif k > slen:
        return 0
    studss = sorted(studs)
    studss.reverse()
    return sum(studs)-sum(studss[slen-(slen%k):])

def strengthss(studs, n):
    res = [strengths(studs, nn) for nn in range(1, n+1)]
    return res

def regstrengths(students, n):
    res = []
    for uni in students:
        res.append(strengthss(uni, n))
    result = [sum([res[u][s] for u in range(len(students))]) for s in range(n)]
    return result

for i in range(t):
    n = int(input())
    u = list(map(int, input().split()))
    s = list(map(int, input().split()))
    students = []
    
    un = set(u)
    unn = list(un)
    for j in range(len(un)):
        students.append([])
    for nn in range(n):
        selected = unn.index(u[nn])
        students[selected].append(s[nn])
    print(*regstrengths(students, n))
        
    
    
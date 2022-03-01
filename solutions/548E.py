n, m = list(map(int, input().split()))
p = list(map(int, input().split()))
c = list(map(lambda x: int(x)-1, input().split()))
d = int(input())
k = []
for dd in range(d):
    k.append(int(input())-1)
    
clubs = [[] for i in range(m)]
clubs_p = [[] for i in range(m)]

def club_add(i):
    clubs[c[i]].append(i)
    clubs_p[c[i]].append(p[i])

irrelevant = list(map(club_add, range(n)))

def find_mex(clubs_p):
    mexed = []
    mex = 0
    while True:
        replace = False
        mexing = True
        if mex not in p:
            return mex
        
        for club in clubs_p:
            if clubs_p.index(club) in mexed:
                continue
            if mex in club:
                index = clubs_p.index(club)
                mexed.append(index)
                mex +=1
                mexing = False
                break
            
        if mexing == True:
            for mexed_club in mexed:
                if mex in clubs_p[mexed_club]:
                    for club in clubs_p:
                        if clubs_p.index(club) in mexed:
                            continue
                        if mexed.index(mexed_club) in club:
                            index = clubs_p.index(club)
                            mexed_club = index
                            replace = True
                            mex +=1
                            break
                        
            if replace == False:
                return mex

for day in range(d):
    club = c[k[day]]
    index = clubs[club].index(k[day])
    clubs[club].remove(k[day])
    clubs_p[club].pop(index)
    team = find_mex(clubs_p)
    print(team)
    
    
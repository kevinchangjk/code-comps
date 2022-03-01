from collections import Counter

nm = list(map(int, input().split()))

n, m = nm[0], nm[1]
laces = []
counted = []

for i in range(m):
    lace = input()
    laces.append(lace)
    counted.extend(lace.split())

kicked = True
kicking = 0

while kicked:
    kicked = False
    count = Counter(counted)
    for person in count:
        if count[person] == 1:
            kicked = True
            while person in counted:
                index = counted.index(person)
                if index % 2 == 0:
                    counted.pop(index)
                    counted.pop(index)
                elif index % 2 == 1:
                    counted.pop(index)
                    counted.pop(index-1)

    if kicked == True:
        kicking +=1
    else:
        break

print(kicking)

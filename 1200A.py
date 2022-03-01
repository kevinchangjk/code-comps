n = int(input())

order = list(input())

rooms = [0 for i in range(10)]

for s in order:
    if s == "L":
        for i in range(10):
            if rooms[i] == 0:
                rooms[i] = 1
                break
    elif s == "R":
        for i in range(10):
            if rooms[9-i] == 0:
                rooms[9-i] = 1
                break
    else:
        rooms[int(s)] = 0
    
print("".join(list(map(str, rooms))))
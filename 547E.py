Hn = list(map(int, input().split()))
H, n = Hn[0], Hn[1]
time = 1
di = list(map(int, input().split()))
health = H
damage = sum(di)

if H == 0:
    print(1)
    
else:
    

    for d in di:
        health +=d
        time +=1
        if health <= 0:
            print(time)
    
    if health >=0:
        if damage >=0:
            print(-1)
        else:
            time = ((H // -damage)-1) * n
            health = H%(-damage) - damage
            di.extend(di)
            for d in di:
                health +=d
                time +=1
                if health <= 0:
                    print(time)
                    break
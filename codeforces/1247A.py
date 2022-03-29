da, db = list(map(int, input().split()))

if da == 9 and db == 1:
    print(str(99)+" "+str(100))

else:

    if db-da > 1 or db-da < 0:
        print(-1)
    
    else:
        if db-da == 1:
            print(str(da)+"9"+" "+str(db)+"0")
        elif db-da == 0:
            print(str(da)+"0"+" "+str(db)+"1")
        

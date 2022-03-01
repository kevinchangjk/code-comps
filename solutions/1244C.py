n,p,w,d = list(map(int, input().split()))

imposs = False
if n*w < p:
    imposs = True
    print(-1)
    
else:
    x = p//w
    y = 0
    z = n-x
    count = x*w + y*d
    rem = p-count
    
    while rem !=0:
        if x<0:
            imposs = True
            break
        x-=1
        rem+=w
        y+=(rem//d)
        rem%=d
        
    if imposs:
        print(-1)
    else:
        print(f"{x} {y} {z}")
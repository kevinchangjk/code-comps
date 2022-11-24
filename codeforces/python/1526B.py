t = int(input())

for i in range(t):
    x = int(input())
    calc = 1
    while calc:
        if x < 100:
            if x % 11 == 0:
                print("YES")
                calc = 0 
            else:
                print("NO")
                calc = 0
        elif x < 1000:
            d = int(str(x)[:2])
            divi = d//11
            rem = d%11
            x = int(str(rem)+(str(x)[2:]))
            if x%11 <= divi:
                print("YES")
                calc = 0
            else:
                print("NO")
                calc = 0
        else:
            div = int(str(x)[:2])//11
            if div == 0:
                rem = str(int(str(x)[:3])%11)
                x = int(rem+str(x)[3:])
            else:
                x -= (div*11*10**(len(str(x))-2))
                
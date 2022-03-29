count = 0
i = 0
words = list(input())
while i+1< len(words) and len(words)>=2:
    if words[i] == words[i+1]:
        count +=1
        del words[i:i+2]
        i-=1
        if i<0:
            i = 0
    else:
        i+=1
        
if count%2 ==0:
    print("No")

else:
    print("Yes")
    
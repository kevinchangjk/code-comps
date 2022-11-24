num = list(map(int, input()))
num.reverse()
i = 0
product = 1

while i < len(num):
    if num[i] == 0:
        
    if num[i] == 9:
        i +=1
        product *= 9
        continue
    else:
        if num[i] * num[i+1] < 9 * (num[i+1] - 1):
            product *= 9 * (num[i+1]-1)
        else:
            product *= num[i] * num[i+1]
            
        i +=2
        
print(product)
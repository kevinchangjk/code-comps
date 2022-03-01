n = int(input())
a = list(map(int, input().split()))
q = int(input())
results = []

def test(lis):
    if lis == []:
        return "NO"
    counter = [0 for i in range(max(lis))]
    rect = 0
    square = 0
    
    for thing in lis:
        counter[thing-1] +=1

    for i in range(len(counter)):
        if counter[i] >= 4:
            counter[i]-=4
            square = 1
            break
        
    for count in counter:
        if count >=4: 
            rect = 2
        elif count >=2:
            rect +=1
        if rect == 2:
            break
    
    if square == 1 and rect == 2:
        return "YES"
    else: 
        return "NO"

for i in range(q):
    sign, length = input().split()
    if sign == '+':
        a.append(int(length))
    else: 
        a.remove(int(length))
    results.append(test(a))
    
print("\n".join(results))
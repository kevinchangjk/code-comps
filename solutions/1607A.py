t = int(input())

for _ in range(t):
    keyboard = input()
    s = input()
    prev = keyboard.index(s[0])
    length = len(s)
    count = 1
    res = 0

    for letter in s[1:]:
        pos = keyboard.index(letter)
        if count < length:
            res += abs(pos-prev)
            prev = pos
            count += 1
        else:
            break
        
    print(res)
        
    

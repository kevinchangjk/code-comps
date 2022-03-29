from collections import Counter

t = int(input())

for i in range(t):
    res = 'YES'
    px, py = list(map(int, input().split()))
    x, y = [0, 0]
    s = input()
    
    ss = Counter(s)
    
    x_range = [-1*ss['L'], ss['R']]
    y_range = [-1*ss['D'], ss['U']]
        
    if x_range[0] <= px <= x_range[1] and y_range[0] <= py <= y_range[1]:
        res = 'YES'
        
    else:
        res = 'NO'
    
    print(res)
one = int(input())
two = int(input())
three = int(input())
four = int(input())

def solve():
    if one >0:
        if one == four:
            return 1
        else:
            return 0
        
    else:
        if three+four == 0:
            return 1
        else:
            return 0

print(solve())
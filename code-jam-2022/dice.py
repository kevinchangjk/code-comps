t = int(input())

def solve():
    n = int(input())
    dice = sorted(list(map(int, input().split())))
    curr = 0

    for die in dice:
        if die > curr:
            curr += 1

    return curr

for i in range(t):
    print(f"Case #{i + 1}: {solve()}")

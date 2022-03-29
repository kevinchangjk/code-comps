t = int(input())

for i in range(t):
    n, q = list(map(int, input().split()))
    s = input()
    
    for i in range(q):
        l, r = list(map(int, input().split()))
        substring = s[(l-1):r]
        if substring[0] in s[:(l-1)]:
            print("YES")
        elif substring[-1] in s[r:]:
            print("YES")
        else:
            print("NO")
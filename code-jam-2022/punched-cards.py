t = int(input())

for i in range(t):
    r, c = map(int, input().split())
    print(f"Case #{i+1}:")
    if r == 0 or c == 0:
        continue
    print(".."+"+-"*(c-1)+"+")
    print(".."+"|."*(c-1)+"|")
    for row in range(r-1):
        print("+-"*c+"+")
        print("|."*c+"|")
    print("+-"*c+"+")

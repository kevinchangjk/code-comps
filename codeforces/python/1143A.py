n = int(input())
doors = list(map(int, input().split()))

doors.reverse()

one = doors.index(1)
zero = doors.index(0)

print(n-(max([one, zero])))
    
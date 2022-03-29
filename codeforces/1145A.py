n = int(input())
a = list(map(int, input().split()))

conc = []

maxi = [16, 1, 2, 1, 4, 1, 2, 1, 8, 1, 2, 1, 4, 1, 2, 1]
streaks = []

if sorted(a) == a:
    print(len(a))
    
elif sorted(a, reverse = True) == a:
    print(1)

else:
    for j in range(0, len(a)-1):
        streak = 0
        for i in range(1, len(a)-j):
            if a[j+i] >= a[j+i-1]:
                streak +=1
        streaks.append(min([streak, maxi[j]]))
                
    print(max(streaks))
    
    
    

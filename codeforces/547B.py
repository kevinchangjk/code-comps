n = int(input())
ai = list(map(int, input().split()))

streaks = [0]
streaking = False
ai.extend(ai)

for a in ai:
    if streaking == False:
        if a == 1:
            streak = 1
            streaking = True
        else:
            continue
    else:
        if a == 1:
            streak +=1
        else:
            streaks.append(streak)
            streaking = False
        
print(max(streaks))
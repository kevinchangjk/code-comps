a, b = list(map(int, input().split()))

wins = 0
draws = 0
losses = 0

for i in range(1, 7):
    ascore = abs(a-i)
    bscore = abs(b-i)
    if ascore < bscore:
        wins +=1
    elif ascore > bscore:
        losses +=1
    else:
        draws +=1
        
print(f"{wins} {draws} {losses}")
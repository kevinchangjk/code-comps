n = int(input())

feeling = ['I hate']

hate = 'that I hate'
love = 'that I love'

for i in range(2, n+1):
    if i%2 == 0:
        feeling.append(love)
    else:
        feeling.append(hate)
        
feeling.append('it')

print(" ".join(feeling))
n = int(input())
s = list(map(int, input()))
count = 0

for i in range(n):
    if s[i] % 2 == 0:
        count += (i+1)
    
print(count)
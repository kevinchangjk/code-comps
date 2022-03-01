n = int(input())

s = input()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

dist = []

for i in range(n-3):
    test = s[i:i+4]
    target = "ACTG"
    dis = [min(abs(alphabet.index(test[j])-alphabet.index(target[j])), 26-abs(alphabet.index(test[j])-alphabet.index(target[j]))) for j in range(4)]
    dist.append(sum(dis))
    
print(min(dist))
from collections import Counter

alphabet = 'abcdefghijklmnopqrstuvwxyz'
n = int(input())
lines = []

for i in range(n):
    lines.append(input())
    
def test(line):
    stop = 0
    
    for char in alphabet:
        if char in line:
            start = alphabet.index(char)
            break
    for char in alphabet[start+1:]:
        if char not in line:
            stop = alphabet.index(char)
            break
    if stop == 0:
        stop = 26
    if stop-start == len(line):
        return "YES"
    else:
        return "NO"


res = list(map(test, lines))
print("\n".join(res))
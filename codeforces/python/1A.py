inputs = input().split()
n = int(inputs[0])
m = int(inputs[1])
a = int(inputs[2])

if n % a == 0:
    nn = n // a
else:
    nn = (n // a) + 1
    
if m % a == 0:
    mm = m // a
else:
    mm = (m // a) + 1
    
print(mm*nn)
t = int(input())

def cd(a, b):
    i = 2
    while i <= min(a, b):
        if a % i == 0 and b % i == 0:
            return 1
        else:
            i += 1

def gcdsum(x):    
    summ = sum(list(map(int, str(x))))
    if cd(x, summ) == 1:
        return 1

def gcdsumf(n):
    while True:
        if gcdsum(n) == 1:
            return n
        else:
            n += 1
            
nn = [int(input()) for i in range(t)]

res = [gcdsumf(n) for n in nn]

print(*res)
    
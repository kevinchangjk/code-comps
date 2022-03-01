n = int(input())

bills = 0

types = [100, 20, 10, 5, 1]

for bill in types:
    bills += n // bill
    n %= bill
    
print(bills)
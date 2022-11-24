n = int(input())
nums = list(map(int, input().split()))
palindromic = True
listed = {0:0}

for num in nums:
    if num not in listed.keys():
        listed[num] = 1
    else:
        listed[num] +=1
    
    if listed[num] == 4:
        listed[num] = 0
        
if n % 2 == 0:
    if sum(listed.values()) != 0:
        palindromic = False

else:
    if sum(listed.values()) != 1:
        palindromic = False

if palindromic:
    print('YES')
    
    if n % 2 == 0:
        nums = sorted(nums)
        
else:
    print('NO')
    
q = int(input())
nums = []
for i in range(q):
    nums.append(input())

for i in range(int(q)):
    l_1, r_1, l_2, r_2 = map(int, nums[i].split(" "))
    
    if l_1 <= l_2:
        print(str(l_1)+" "+str(r_2))
    else:
        print(str(r_1)+" "+str(l_2))
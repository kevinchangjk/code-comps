nums = input().split(" ")
num = int(nums[0])
k = int(nums[-1])

def solve(k, num):
    for i in range(k):
        if num%10 == 0:
            num = int(num/10)
        else:
            num -=1
    return num

print(solve(k, num))
def solve(k, str1, str2):
    curr_str = str1
    r = 0
    prev = 0
    index = 0
    for letter in str2:
        if letter not in str1:
            return "NO"
        if letter not in curr_str:
            curr_str = str1
            r += 1
            index = curr_str.index(letter)
            prev = 0
        else:
            index = curr_str.index(letter)
        
        if index < prev:
            curr_str = str1
            r += 1
        curr_str = curr_str[:index] + curr_str[index + 1:]
        prev = index

    if r <= k:
        return "YES"
    else:
        return "NO"


t = int(input())
for i in range(t):
    k = int(input())
    str1 = input()
    str2 = input()
    print(solve(k, str1, str2))

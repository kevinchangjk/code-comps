def solve(N, A):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    store = {}
    total_sum = 0
    
    for string in A:
        str_len = len(string)
        letter = string[0]
        if letter not in alphabet:
            total_sum += int(letter) + 10 ** (str_len - 1)
        else:
            if letter not in store:
                store[letter] = [True, 0]
            store[letter][0] = False
            store[letter][1] += 10 ** (str_len - 1)

        for i in range(1, str_len):
            letter = string[i]
            if letter not in alphabet:
                total_sum += int(letter) * 10 ** (str_len - i - 1)
            else:
                if letter not in store:
                    store[letter] = [True, 0]
                store[letter][1] += 10 ** (str_len - i - 1)
        
        weights = sorted(store.values(), key=lambda arr: arr[1], reverse=True)
        digits = list(range(10))
        for weight in weights:
            if digits[0] == 0 and not weight[0]:
                total_sum += weight[1] * digits.pop(1)
            else:
                total_sum += weight[1] * digits.pop(0)

    return total_sum


t = int(input())
for i in range(t):
    N = int(input())
    A = list(input().split())
    print(solve(N, A))

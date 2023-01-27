# Template for Codeforces problems
# By @kevinchangjk

import sys
input = sys.stdin.readline

# ---- Input Functions ---- #


# takes in a single integer
def inp():
    return(int(input()))


# reads and returns a list of integers
def inlt():
    return(list(map(int, input().split())))


# reads and returns a list of characters, or essentially a string
def insr():
    s = input()
    return(list(s[:len(s) - 1]))


# returns space separated integers, instead of a list
def invr():
    return(map(int, input().split()))


# first input: usually no. of test cases
tc = inp()


# solution
def solve():
    n = inp()
    perms = []
    digits = dict()
    for i in range(n):
        perm = inlt()
        perms.append(perm)
        start = perm[0]
        if start not in digits:
            digits[start] = 0
        digits[start] += 1

    full_perm = []
    for digit in digits.keys():
        if digits[digit] > 1:
            full_perm.append(digit)
    
    for perm in perms:
        if perm[0] != full_perm[0]:
            full_perm.extend(perm)
    
    print(*full_perm)


# running loop for each test case
for t in range(tc):
    solve()

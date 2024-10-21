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
    return s.rstrip()

# returns space separated integers, instead of a list
def invr():
    return(map(int, input().split()))


# first input: usually no. of test cases
tc = inp()


# solution
def solve():
    a, b = insr(), insr()
    len_a, len_b = len(a), len(b)
    index = 0
    while index < min(len_a, len_b):
        if a[index] != b[index]:
            break
        index += 1

    result = len_a + len_b - index

    if index > 0:
        result += 1

    print(result)

# running loop for each test case
for t in range(tc):
    solve()

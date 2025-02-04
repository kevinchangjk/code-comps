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
    a = inlt()
    b = inlt()

    a_set = set(a)
    b_set = set(b)

    if len(a_set) * len(b_set) >= 3:
        print("YES")
    else:
        print("NO")


# running loop for each test case
for t in range(tc):
    solve()

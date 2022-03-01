nk = list(map(int, input().split()))
n, k = nk[0], nk[1]
moves = 0

if k <= n//2:
    moves += k-1

else:
    moves += n-k

moves += 3 * n

print(moves)

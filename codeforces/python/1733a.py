t: int = int(input())


def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    maximum_arr = [0 for i in range(k)]

    for i in range(n):
        index = i % k
        maximum_arr[index] = max(arr[i], maximum_arr[index])

    res = sum(maximum_arr)
    return res


for _ in range(t):
    res = solve()
    print(res)

t = int(input())

for i in range(t):
    n, m, jj, j = list(map(int, input().split()))
    corners = [[1, 1], [1, m], [n, 1], [n, m]]
    mapping = [0, 3, 0, 1, 2, 1]
    diff = list(map(lambda x: sum([abs(jj-x[0]), abs(j-x[1])]), corners))
    closest = diff.index(min(diff))
    res = corners[closest]
    res2 = corners[mapping.index(closest)+1]
    res.extend(res2)
    print(*res)
    
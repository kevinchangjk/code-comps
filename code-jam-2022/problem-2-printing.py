t = int(input())

def solve():
    printer1 = list(map(int, input().split()))
    printer2 = list(map(int, input().split()))
    printer3 = list(map(int, input().split()))

    c = [printer[0] for printer in [printer1, printer2, printer3]]
    m = [printer[1] for printer in [printer1, printer2, printer3]]
    y = [printer[2] for printer in [printer1, printer2, printer3]]
    k = [printer[3] for printer in [printer1, printer2, printer3]]

    total = 0
    res = []
    c_min = min(c)
    m_min = min(m)
    y_min = min(y)
    if total + c_min > 10**6:
        res.append(10**6 - total)
        total = 10**6
    else:
        res.append(c_min)
        total += c_min
    if total + m_min > 10**6:
        res.append(10**6 - total)
        total = 10**6
    else:
        res.append(m_min)
        total += m_min
    if total + y_min > 10**6:
        res.append(10**6 - total)
        total = 10**6
    else:
        res.append(y_min)
        total += y_min

    req_k = 10**6 - total

    for k_single in k:
        if k_single < req_k:
            return "IMPOSSIBLE"

    res.append(req_k)
    return " ".join(map(str, res))

for i in range(t):
    print(f"Case #{i + 1}: {solve()}")

from collections import Counter

n = int(input())
a_s = list(map(int, input().split()))

count = Counter(a_s)
count = [count[x] for x in sorted(count.keys())]
group_count = [sum(count[i-2:i+3]) if i+3 < n else sum(count[i-2:]) for i in range(2, n-2)]

print(max(group_count))



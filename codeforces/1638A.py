t = int(input())

for _ in range(t):
  n = int(input())
  p = list(map(int, input().split()))
  target = 0
  findTarget = True

  i = 0
  while findTarget and i < n:
    if p[i] == i + 1:
      i += 1
      continue
    else:
      target = i
      findTarget = False

  key = p.index(target + 1)
  if target == key:
    print(*p)
  else:
    p_reverse = p[target:key+1]
    p_reverse.reverse()
    res = p[:target] + p_reverse + p[key + 1:]
    print(*res)

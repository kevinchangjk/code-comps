t=int(input())
for i in range(t):
	n=int(input())
	a=list(map(int,input().split()))
	s=0
	for x in a:
		s ^= x
	if s==0:
		print('YES')
	else:
		c=0
		ps=0
		for i in range(n):
			ps ^= a[i]
			if ps == s:
				c+=1
				ps=0
		if c>=2:
			print("YES")
		else:
			print("NO")
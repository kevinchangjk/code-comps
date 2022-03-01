t = int(input())
 
for i in range(t):
	n = int(input())
	layout = []
	coords = []
	for j in range(n):
		s = list(input())
		layout.append(s)
		for k in range(len(s)):
			if s[k]== "*":
				coords.append([j, k])
			else: 
				pass
				
	if coords[0][0] == coords[1][0]:
		jj = coords[0][0]
		kk, kkk = coords[0][1], coords[1][1]
		
		if jj < n-1:
			layout[jj+1][kk], layout[jj+1][kkk] = "*", "*"
		else: 
			layout[jj-1][kk], layout[jj-1][kkk] = "*", "*"
	elif coords[0][1] == coords[1][1]:
		jj, jjj = coords[0][0], coords[1][0]
		kk = coords[0][1]
		if kk != 0:
			layout[jj][kk-1], layout[jjj][kk-1] = "*", "*"
		else: 
			layout[jj][kk+1], layout[jjj][kk+1] = "*", "*"
	else: 
		jj, jjj = coords[0][0], coords[1][0]
		kk, kkk = coords[1][1], coords[0][1]
		layout[jj][kk], layout[jjj][kkk] = "*", "*"
	layout = ["".join(lay) for lay in layout]
	print("\n".join(layout))
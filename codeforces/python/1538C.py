"""
t = int(input())

for i in range(t):
    n, l, r = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a = sorted([aa for aa in a if aa<r])
    pairs = 0
    for j in range(len(a)):
        for k in range(j+1, len(a)):
            if l <= a[j]+a[k] <= r:
                pairs += 1
            elif a[j] + a[k] > r:
                break
    print(pairs)
    
"""
R=lambda:map(int,input().split())
t,=R()
while t:
 t-=1;n,l,r=R();a=sorted(R());i=j=q=0
 while i<n:
  n-=1
  while i<n and a[i]+a[n]<l:i+=1
  while j<n and a[j]+a[n]<=r:j+=1
  q+=min(j,n)-i
 print(q)
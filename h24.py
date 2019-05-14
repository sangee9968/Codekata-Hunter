n,k=map(int,input().split())
l=list(map(int,input().split()))
a=1
for i in range(0,len(l)-1):
	if l[i]+l[i+1]==k:
		a=0
if a==0:
	print("YES")
else:
  #result
	print("NO")
	

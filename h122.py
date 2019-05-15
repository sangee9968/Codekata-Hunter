n=int(input())
l=list(map(int,input().split()))
s1=0
s2=0
l1=[]
a=1
for i in range(1,len(l)):
	s1=sum(l[0:i])
	s2=sum(l[i+1:len(l)])
	if s1==s2:
		a=0
		break
if a==0:
	print("yes")
else:
  #result
	print("no")

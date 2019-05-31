#inputn=int(input())
l=list(map(int,input().split()))
l1=[]
s=" "
for i in range(n-1):
	c=l[i+1:]
	l1.append(str(max(c)))
l1.append("0")
print(s.join(l1))


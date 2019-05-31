#input
s=input()
l=list(s.split())
m=[]
for i in range(len(l)):
	if i%2==0:
		c=l[i]
		m.append(c[::-1])
	else:
		m.append(l[i])
print(*m)		
		

#input
s=input()
if s[-1]==".":
	s=s[:-1]
l=list(s.split())
m=[]
for i in range(len(l)):
	if i%2==0:
		c=l[i]
		m.append(c[::-1])
	else:
		m.append(l[i])
print(*m)		
		

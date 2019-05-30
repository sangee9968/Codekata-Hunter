#input
n=int(input())
a=0
l=[]
for i in range(2,n):
	for j in range(2,i+1):
		if i%j==0:
			break
	if i==j:
		l.append(i)
for i in range(len(l)):
	for j in range(len(l)):
		for k in range(len(l)):
			if l[i]+l[j]+l[k]==n:
				print(str(l[i])+" "+str(l[j])+" "+str(l[k]))
				a=1
				break
		if a==1:
			break
	if a==1:
		break

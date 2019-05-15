n=int(input())
l=[]
sum=0
for i in range(2,n+1):
	for j in range(2,i):
		if i%j==0:
			break
	else:
		l.append(i)
for i in l:
	if i%10==3:
		sum=sum+i
#result    
print(sum)	

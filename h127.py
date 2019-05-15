s,a=map(str,input().split())
l=[]
l1=[]
for i in range(0,len(a)+1):
	for j in range(i+1,len(a)+1):
		l.append(a[i:j])
for i in l:
	if i in s:
		l1.append(len(i))
#result    
print(l[l1.index(max(l1))])	

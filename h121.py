s=input()
l=[]
l1=[]
s1=""
for i in range(0,len(s)+1):
	for j in range(i+1,len(s)+1):
		l.append(s[i:j])
print(l)		
for i in l:
	if i[::-1]==i:
		l1.append([i,len(i)])
for i in range(0,len(l1)):		
	 l1.sort(key = lambda x: x[1],reverse=True) 
#result   
print(l1[0][0])	
	

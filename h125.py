s=input()
l=list(s)
l1=[]
for i in l:
	l1.append([l.count(i),i])
for i in range(0,len(l1)):
	if l1[i][0]==1:
    #result
		print(l1[i][1],end="")

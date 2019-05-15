n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(0,len(l)):
	l1.append([l.count(l[i]),l[i]])
l1.sort(key=lambda x:x[0],reverse=True)
#result
print(l1[0][1])

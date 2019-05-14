n=int(input())
l=list(map(int,input().split()))
l1=l[::-1]
s=""
for i in l1:
	s=s+str(i)+"->"
#result  
print(s[0:len(s)-2])	

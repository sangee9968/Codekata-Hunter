n=int(input())
c=0
l=list(map(int,input().split()))
for i in range(0,len(l)):
    if i==l[i]:
        s=s+str(i)+" "
        c=c+1
#result        
print(s.strip()) 
if c==0:
    #result
    print("-1")

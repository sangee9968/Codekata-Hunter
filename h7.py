n=int(input())
s=""
l=list(map(int,input().split()))
for i in range(0,len(l)):
  if i%2==0 and l[i]%2==1 or i%2==1 and l[i]%2==0:
    s=s+str(l[i])+" "
#result    
print(s.strip())    

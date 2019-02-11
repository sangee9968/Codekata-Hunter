n=int(input())
l=list(map(int,input().split()))
l1=[]
l1=list(set(l))
for j in range(0,len(l1)):
  if l.count(l1[j])==1:
    #result
    print(l1[j])
         

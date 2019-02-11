n=int(input())
l=list(map(int,input().split()))
l1=[0,1]
for i in range(0,len(l)):
  for j in range(i+1,len(l)):
    if l[i]+l[j]==0:
      print(l[i],l[j])
      break
    elif l[i]<0 or l[i]<0:
      if l[i]+l[j]==-1 or l[i]+l[j]==1:
        print(l[i],l[j])  
        break

n=int(input())
l=list(map(int,input().split()))
l1=[0]
for i in range(0,len(l)):
  for j in range(i+1,len(l)):
    if l[i]+l[j] in l1:
      #result
      print(l[i],l[j])

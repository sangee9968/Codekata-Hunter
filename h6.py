n=int(input())
l1=[]
l=list(map(int,input().split()))
if len(l)==len(set(l)):
  print("unique")
else:
  for i in range(0,len(l)):
    if l.count(l[i])>1:
      l1.append(l[i])
  #result    
  print(l1[0])
    

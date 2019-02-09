n=int(input())
l=list(map(int,input().split()))
l1=[]
l1=list(set(l))
for i in l:
    for j in l1:
       if l.count(j)==1:
          print(i)
         

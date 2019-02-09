n=int(input())
c=0
s=""
l=list(map(int,input().split()))
for i in range(0,len(l)):
    if i==l[i]:
       print(''.join(str(i)),end=" ")
       c=c+1
if c==0:
    #result
    print("-1")

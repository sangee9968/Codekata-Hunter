n=int(input())
c=0
l=list(map(int,input().split()))
for i in range(0,len(l)):
    if i==l[i]:
        print(i,end=" ")
        c=c+1
if c==0:
    #result
    print("-1")

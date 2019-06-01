#input
n=int(input())
l1=[]
c=0
for i in range(n):
   l=list(map(int,input().split()))
   l1.append(l)
for i in range(n):
    for j in range(n):
        if i==j:
            c=c+l1[i][j]
print(c)

l1=[]
n=int(input())
l=list(map(int,input().split()))
l.sort()
ml=list(set(l))
for i in range(len(ml)):
        if (l.count(ml[i]) > 1 ):
          l1.append(ml[i])
#result          
print(' '.join(map(str,l1)))

n,k=map(int,input().split())
l=list(map(int,input().split()))
l.sort(reverse=True)
#result
print(l[k-1])

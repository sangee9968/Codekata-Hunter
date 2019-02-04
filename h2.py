n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
#result
print(''.join(map(str,l)))

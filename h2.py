n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
if all(i==0 for i in l):
    print("0")
else:
    #result
    print(''.join(map(str,l)))

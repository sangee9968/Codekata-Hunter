n=input()
l=list(map(int,input().split()))
u,v=map(int,input().split())
if u in l and v in l:
  #result
	print(abs(l.index(u)-l.index(v)))

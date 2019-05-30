#input
n=int(input())
sum=0
m=len(str(n))
while n>0:
	r=int(n)%10
	sum=sum+(r**m)
	n=n//10
print(sum)

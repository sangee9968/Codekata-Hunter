#input
s=input()
a=1
if len(s)==1:
	print("yes")
else:
	for j in s:
		if s.count(j)==len(s):
			print("no")
			a=0
			break
	if a==1:
		print("yes")

s=input()
l=[]
for i in range(0,len(s)-1):
	for j in range(i+1,len(s)):
		a=s[i:j+1]
		b=a[::-1]
		if a==b:
			l.append(a)
for i in l:
  #result
	print(i)

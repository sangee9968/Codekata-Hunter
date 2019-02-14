s=input()
l=list(s.split())
s1=""
for i in l:
  s1=s1+str(i[::-1])+" "
#result  
print(s1.strip())   

#input
s=input()
s1=''
for i in range(0,len(s)-1,2):
  if int(s[i+1])%2==0:
    s1+=s[i]*int(s[i+1])
  else:
    s1+=s[i]+s[i+1]
print(s1)

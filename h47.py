import re
#input
s=input()
r=re.sub(' +', ' ',s)
print(r.strip())

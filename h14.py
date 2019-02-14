from itertools import permutations
s=input()
p=permutations(s)
for i in list(p):
    #result
    print(''.join(i))

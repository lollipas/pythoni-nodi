import sys
import re
p=sys.argv
s = 0
for l in p:
    if re.search("[0-9]",l) or re.search("[!#$%&()=' ']",l):
        s+=3
    if re.search("[A-Z]",l):
        s+=2
    if re.search("[a-z]",l):  
        s+=1
print(s)
print(sys.argv)
        
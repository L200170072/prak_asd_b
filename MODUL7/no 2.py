import re

f = open("Indonesia.txt", "r")
p = r'di[\w\.-]+'
string2 = re.findall(p, f.read())
print (string2)

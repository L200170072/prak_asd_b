import re

f = open("Indonesia.txt", "r")
p = r'me[\w\.-]+'
string = re.findall(p, f.read())
print (string)

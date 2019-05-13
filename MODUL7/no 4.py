import re
f = open ('KEI.html', 'r', encoding='latin1')

teks = f.read()

strings = re.findall(r'title="([\w+]+)">', teks)
strings = re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>', teks)
a = []
for i in strings:
    a.append((i[0], float(i[1])))

print(a)

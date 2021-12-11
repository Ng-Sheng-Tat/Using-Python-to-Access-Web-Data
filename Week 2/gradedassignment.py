import re
var = open('actualdata.txt')
emptylist = list()

for line in var:
    line = line.rstrip()
    # print(line)
    y = re.findall('[0-9]+', line)
    # print(y)
    emptylist += y
ans = 0
for num in emptylist:
    ans += int(num)
print(ans)
print(len(emptylist))

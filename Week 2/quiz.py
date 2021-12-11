x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
import re
# Questions 1
# y = re.findall('@\S+', x)
# print(y) # ['@uct.ac.za']
y = re.findall('@(\S+)', x)
print(y) # ['uct.ac.za']
# y = re.findall('..@\S+..', x)
# print(y) ['rd@uct.ac.za S']
# y = re.findall('F.+:')
# Questions 2
y = re.findall('\S+?@\S+', x)
print(y)

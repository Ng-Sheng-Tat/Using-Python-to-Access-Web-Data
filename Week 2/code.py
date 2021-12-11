var = open('mbox-short.txt')
import re
# First Lecture
# Example 1
# Methods 1
# for line in var:
#     line = line.rstrip()
#     if line.find('From:') >= 0:
#         # print(line)
#         pass
#     print(line.find('From:'))

# Methods 2
# for line in var:
#     line = line.rstrip()
#     if re.search('From:', line):
#         print(line)
#     print(re.search('From:', line))

# Eg 2
## line.startswith('From:')
# for line in var:
#     line = line.rstrip()
#     if re.search('From:', line):
#         print(line)
# ^X.*:
# start with X
# any character with match any character
# * means many time
# until : is reached

# X-abc abc:
# fail for
# ^X-\s+:
# \s means any-non charater, + means one or more times

# Second videos
x = 'My 2 favourite numbers are 19 and 20. '
y = re.findall('[0-9]+', x) # one or more digit
y = re.findall('[aeuouM]+', x)
# print(y)

# Greedy Match
x = 'From : Using the : something to write'
y = re.findall('^F.+:', x)
# print(y)

# Non-greedy match
x = 'From: Using the : something to write'
x = 'From: Using the :Fomethingtowrite:'
y = re.findall('^F.+?:', x)
# print(y)

# Greedy match emails
x = 'From shotna.faofna@sanofns.as.sa safiabf'
y = re.findall('\S+@\S+', x)
# Bracket means I only want that
y = re.findall('^From (\S+@\S+)', x)
# print(y)

x = "From stephen.marquesomethign@fnaonf.fanofn anfoafeoa"
word = x.split()
# print(word)
piece = word[1].split('@')
# print(piece)

# means not [^ ] - match non-blank character
x = 'From stonsaogn@gnaon.anogfa anfoi asngofn 296581'
y = re.findall('@([^ ]*)', x)
y = re.findall('From .*@([^ ]*)', x)
# print(y)

# Span Confidence
numlist = list()
for line in var:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    # one or more time --> ([0-9.]+)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))
# \$ means the real dollar sign

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = int(input("Enter count: "))
pos = int(input("Enter Position: "))

url = input('Enter - ')
for i in range(count):
    pos2 = 0
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        url = tag.get('href', None)
        pos2 += 1
        if pos2 == pos:
            break

    print(url)
y = re.findall('by_(.*).html', url)
print(y[0])

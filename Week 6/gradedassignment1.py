from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
data = BeautifulSoup(html, "html.parser")
# http://py4e-data.dr-chuck.net/comments_42.json

data = str(data)
# print(data)
info = json.loads(data)
# print('User count:', len(info))
count = 0
for data in info['comments']:
    count += data['count']
print(count)

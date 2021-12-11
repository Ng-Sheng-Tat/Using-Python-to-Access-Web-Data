import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter location: ')

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()

data = data.decode()
tree = ET.fromstring(data)
# print(tree)

count = 0
total = 0

results = tree.findall('comments/comment')
# results = tree.findall('.//count')
# print(results)
for tag in results:
    count += 1
    total += int(tag.find('count').text)
#
print('Count:', count)
print('Sum:', total)

import xml.etree.ElementTree as ET
# Example 1
# data = '''
#     <person>
#     <name>Chuck</name>
#     <phone type="intl">
#     +1 734 303 4456
#     </phone>
#     <email hide='Yes'/>
#     </person>'''
# tree = ET.fromstring(data)
# print("Name:", tree.find('name').text)
# print("Attr:", tree.find('email').get('hide'))

# Example 2
input = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="5">
            <id>002</id>
            <name>Brend</name>
        </user>
    </users>
    </stuff>'''

stuff = ET.fromstring(input)
treelist = stuff.findall('users/user')
print('User Count:', len(treelist))
for item in treelist:
    print()
    print('Name:', item.find('name').text)
    print("Id:", item.find('id').text)
    print("Attribute:", item.get("x"))

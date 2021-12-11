import json
# Exmaple 1, json as dictionary
# data = '''{
#     "name": "Chuck",
#     "phone": {
#         "type": "intl",
#         "number": "+1 734 330 4435"
#     },
#     "email" :{
#         "hide": "yes"
#     }
# }'''
#
# info = json.loads(data)
# print('Name:', info['name'])
# print('Hide:', info['email']['hide'])

# Example 2, json as list
input = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

info = json.loads(input) # info is a list
print('User Count:', len(info))
for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Atrribute', item['x'])

import json
input='''[
{ "id":"007",
  "x":"2",
  "name":"Bpnd..James Bond"},
{ "id":"069",
  "x":"3",
  "name":"Cat..Pussy Cat"}
]'''

info=json.loads(input)
print('User Count:',len(info))

for items in info:
  print('Name',items['name'])
  print('Id',items['id'])
  print('Attribute',items['x'])

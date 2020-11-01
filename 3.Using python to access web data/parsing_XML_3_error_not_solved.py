import xml.etree.ElementTree as ET
input='''<stuff>
  <users>
    <user x="2">
      <id>007</id>
      <name>Bond..James Bond</name>
    </user>
    <user x="3">
      <id>069</id>
      <name>Cat..Pussy Cat</name>
    <user>
  </users>
</stuff>'''

stuff=ET.fromstring(input)
lst=stuff.findall('users/user')
print('User count:',len(lst))

for item in lst:
  print('Name',item.find('name').text)
  print('Id',item.find('id').text)
  print('Attribute',item.get("x"))

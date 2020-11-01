import xml.etree.ElementTree as ET
data='''<person>
  <name>Yoho</name>
  <phone type="intl">
    +91 94241 51149
  </phone>
  <email hide="yes"/>
</person>'''

tree=ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))

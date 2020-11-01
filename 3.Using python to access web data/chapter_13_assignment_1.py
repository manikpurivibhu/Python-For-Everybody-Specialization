import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import ssl

total=0

address = input('Enter location: ')

with urllib.request.urlopen(address) as url:
    url=url.read()

stuff=ET.fromstring(url)
lst=stuff.findall('.//count')
print('Count:',len(lst))
for item in stuff.findall(".comments/comment"):

        total=total+int(item.find('count').text)

print('Sum:',total)
#http://py4e-data.dr-chuck.net/comments_42.xml
#http://py4e-data.dr-chuck.net/comments_558227.xml
#used Github

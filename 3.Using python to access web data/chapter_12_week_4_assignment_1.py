import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url=input('Enter URL:')
html=urllib.request.urlopen(url).read()
cute=BeautifulSoup(html,'html.parser')

sum=0


#retieve all the numbers
tags=cute('span')
for tag in tags:

  num=int(tag.contents[0])
  sum=sum+num

print('Sum is ',sum)

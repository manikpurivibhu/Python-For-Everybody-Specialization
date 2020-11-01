import json
import urllib.request, urllib.parse, urllib.error
import ssl

while True:

 sum=0
 c=0
 lst=list()

 #prompt a URL
 url=input('Enter URL:')
 if len(url)<1:  break

 #Ignore SSL Certification Errors
 ctx=ssl.create_default_context()
 ctx.check_hostname=False
 ctx.verify_mode=ssl.CERT_NONE

 #read the JSON data using urllib
 handle=urllib.request.urlopen(url,context=ctx)
 data=handle.read().decode()
 #print(data)

 #parse and extract comment counts from JSON data

 js=json.loads(data)
# print(js)

 for comment in js['comments']:
     no=js["comments"][c]["count"]
     sum+=int(no)
     print(sum)
     c=c+1

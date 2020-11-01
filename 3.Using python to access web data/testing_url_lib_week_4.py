#testing url library
#just for fun
#error not sorted in line 6
import urllib.request, urllib.parse, urllib.error

fhand=urllib.request.urlopen('http://data.pr4e.prg/romeo.txt')

for line in fhand:
  print(linee.decode().strip())

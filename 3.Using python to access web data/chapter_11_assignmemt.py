file=input(':Enter File Name:')
if len(file)<1: file='file.txt'

handle=open(file)
lst=list()
tot=0

import re

for lines in handle:

    output=re.findall('[0-9]+',lines)
    if output==[]:    continue
    output=[int(i) for i in output]

    tot=tot+sum(output)

print(tot)

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fhand = open(name)
dic=dict()

for line in fhand:

  if line.startswith('From '):
    words=line.split()
    per=words[1]
    for word in words:
      dic[per]=dic.get(per,0)+1
      


bigcount=None
bigword=None

for per,count in dic.items():
        if bigcount is None or bigcount<count:
            bigcount=count
            bigword=per
print(bigword,bigcount)

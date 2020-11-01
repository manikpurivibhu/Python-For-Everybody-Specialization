name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dic=dict()

#creating required dictionary with time as key  and count as value
for line in handle:
  if line.startswith('From '):
    words=line.split()
    tim=words[5]
    tim.split(':')
    time=tim[0:2]
    dic[time]=dic.get(time,0)+1

tmp=list()
for time,count in dic.items():
    newt=(count,time)
    tmp.append(newt)


tmp.sort()
#print(tmp)
#print(newt)
for count,time in tmp:
        print(time,count)

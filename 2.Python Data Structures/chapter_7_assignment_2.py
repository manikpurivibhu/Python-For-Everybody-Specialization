fname = input("Enter file name: ")
fh = open(fname)
count=0
total=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count=count+1
    app=line.find('.')
    val=float(line[app-1:app+5])
    total=total+val

print('Average spam confidence:',float(total/count))

largest=None
small=None


while True:
 num =input("Enter a number: ")
 if num == "done" : break
 else:
  n1=int(num)

  print(largest)
  n1= int(num)
  print(small)
 if n1 <small:
  small=n1

 if n1> largest:
  largest=n1


print ("Maximum", largest)
print ("Min", small)

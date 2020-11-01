largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
      break
    else:
      try:
        no=int(num)
      except:
        print('Invalid input')
    if smallest is None:
        smallest=no
    elif smallest>no:
        smallest=no
    elif largest is None:
        largest=no
    elif no>largest:
        largest=no
    elif smallest>largest:
        largest=smallest
print("Maximum is",largest)
print("Minimum is",smallest)

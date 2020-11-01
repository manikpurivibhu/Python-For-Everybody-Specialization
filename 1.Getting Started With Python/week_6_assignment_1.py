hours=input("Enter Hours:")
h=float(hours)
rate=input("Enter Hourly Rate")
r=float(rate)
def computepay():
  if h<=40:
      pay=h*r
  else:
      pay=(40*r)+((h-40)*r*1.5)
  return pay
print('Pay',computepay())

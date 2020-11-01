hours=input("Enter Hours:")
h=float(hours)
rate=input("Enter Hourly Rate")
r=float(rate)
if h<=40:
    pay=h*r
else:
    pay=(40*r)+((h-40)*r*1.5)
print(float(pay))

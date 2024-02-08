hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h>40:
    sup = h-40
    pay = (40*r)+(sup*r*1.5)
else:
    pay = h*r
print(pay)
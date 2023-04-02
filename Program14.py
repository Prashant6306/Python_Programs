"""
Q.14. Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
"""
import datetime

print(datetime.datetime.now())


print(datetime.date.today())

print(datetime.datetime.now().time())


from datetime import date
f_date = date(2014, 7, 2)
print(f_date)
l_date = date(2014, 7, 11)
print(l_date)
delta=l_date-f_date
print(delta)
print(delta.days)
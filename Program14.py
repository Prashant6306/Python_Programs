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
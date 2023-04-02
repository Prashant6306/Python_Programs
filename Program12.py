"""
Q.12. Write a Python program that prints the calendar for a given month and year.
Note : Use 'calendar' module.
"""
import calendar

y=int(input("Enter the year"))
m=int(input("Enter the month"))
d=int(input("Enter the day"))
print(calendar.month(y,m))
print(calendar.monthcalendar(y,m))

print(calendar.isleap(y))

print(calendar.weekday(y,m,d))
var=calendar.weekday(y,m,d)
print(calendar.day_name[var])


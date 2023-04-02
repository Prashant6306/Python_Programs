import datetime

now=datetime.datetime.now()

print(now)

print(now.strftime("%Y"))
print(now.strftime("%m"))
print(now.strftime("%d"))
print(now.strftime("%H"))
print(now.strftime("%M"))
print(now.strftime("%S"))
print(now.strftime(("%Y/%m/%d %H:%M:%S")))
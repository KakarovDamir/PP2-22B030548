import datetime

x = datetime.datetime.now()
y = datetime.datetime(x.year, x.month, x.day + 1)
z = datetime.datetime(x.year, x.month, x.day - 1)

print (z.strftime("%A,"), x.strftime("%A,"), y.strftime("%A"))

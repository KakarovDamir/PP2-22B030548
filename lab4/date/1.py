import datetime

x = datetime.datetime.now()
y = datetime.datetime(x.year, x.month, x.day - 5)

print(y.strftime("%A"))
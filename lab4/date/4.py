import datetime
x = datetime.datetime.now()
day = int(input())
y = datetime.datetime(x.year, x.month, day, x.hour, x.minute, x.second)

timedelta = y - x
print(f"time difference: {timedelta.total_seconds()} seconds")
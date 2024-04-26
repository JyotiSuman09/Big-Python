# Date and time
import datetime
print(dir(datetime))
from datetime import timedelta, datetime, date

now = datetime.now()
print(type(now), now)
day = now.day
month = now.month
timestamp = now.timestamp()
print(timestamp)


# Create a datetime object representing a specific date and time
dt = datetime(2022, 4, 26, 12, 30, 0)

# Convert the datetime object to a timestamp (Unix epoch time)
timestamp = dt.timestamp()

print("Datetime object:", dt)
print("Timestamp:", timestamp)

# Convert the timestamp back to a datetime object
new_dt = datetime.fromtimestamp(timestamp)

print("Converted datetime object:", new_dt)
# Timestamp or Unix timestamp is the number of seconds elapsed from 1st of January 1970 UTC.


t = now.strftime("%H:%M:%S")
print(t)

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print(day)
print(month)
print(year)
print(hour)
print(minute)
print(timestamp)
print("========================="*3, "\n")

curr = now.strftime("%m/%d/%Y, %H:%M:%S")
print(curr)

date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print(date_object)

new_year = date(2025, 1, 1)
print(new_year)
today = date.today()
print(today)

print("Days till new year: ", new_year - today)

given_date = date(1970, 1, 1)
print(given_date)
print("The time difference between 1 January 1970 and now: ", today - given_date)

t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)

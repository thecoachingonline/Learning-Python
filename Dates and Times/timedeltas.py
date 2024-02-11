from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

print(timedelta(days=356, hours=5, minutes=1))

now = datetime.now()
print("Today is", now)

print("One year from now it will be", str(now + timedelta(days=365)))

print("In two weeks and 3 days it will be", str(now + timedelta(weeks=2, days=3)))

t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print("One week ago it was", s)



today = date.today()
afd = date(today.year, 4, 1)

if afd < today:
    print("April Fools' Day already went by:", ((tody-afd).days))
    afd = afd.replace(year= today.year + 1)

time_to_afd = afd - today
print("It is", time_to_afd, "days until the next Aprill Fools' Day!")
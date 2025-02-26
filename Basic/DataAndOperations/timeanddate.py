#!/usr/bin/env python3

import time

timenow = time.localtime(time.time())
year,month,day,hour,minute = timenow[0:5]

print(str(day) + "/" + str(month) + "/" + str(year))
print(str(hour) + ":" + str(minute))

print("Hello")
time.sleep(1)
print("World")
time.sleep(1)
print("🙏สวัสดี")
time.sleep(1)
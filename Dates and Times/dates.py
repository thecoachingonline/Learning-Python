from datetime import date
from datetime import time
from datetime import datetime

def main():

    today  = date.today()
    print("วันนี้ คือ:", today)

    print("วัน/เดือน/ปี คือ:", today.day, today.month, today.year)

    print("สัปดาห์นี้ คือ:", today.weekday())
    days = ["mon","tue","wed","thur","fri","sat","sun"]
    print("Which is a ", days[today.weekday()])

    today = datetime.now()
    print("The current date and time is", today)

    t = datetime.time(datetime.now())
    print("The current time is", t)

if __name__ == "__main__":
    main()
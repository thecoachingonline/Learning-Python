from datetime import date

def calculate_days_left(birth_day, birth_month, birth_year, target_age):
    """คำนวณจำนวนวันที่เหลืออยู่จนถึงอายุเป้าหมาย"""

    today = date.today()
    birth_date = date(birth_year, birth_month, birth_day)

    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    target_year = birth_date.year + target_age
    target_date = date(target_year, birth_month, birth_day)
    days_left = (target_date - today).days

    return days_left

def calculate_time_usage(days_left):
    """คำนวณจำนวนเวลาที่ใช้ในการนอน ทำงาน และเวลาส่วนตัว"""

    hours_sleep = days_left * 8
    hours_work = days_left * 8
    hours_personal = days_left * 8

    return hours_sleep, hours_work, hours_personal

# รับข้อมูลจากผู้ใช้
birth_day = int(input("กรุณาใส่วันเกิด (1-31): "))
birth_month = int(input("กรุณาใส่เดือนเกิด (1-12): "))
birth_year = int(input("กรุณาใส่ปีเกิด (พ.ศ.): "))
birth_year -= 543  # แปลงปี พ.ศ. เป็น ค.ศ.

# คำนวณวันที่เหลือถึงอายุ 60 ปี
days_left_60 = calculate_days_left(birth_day, birth_month, birth_year, 60)
if days_left_60 > 0:
    print(f"คุณเหลือเวลาอีกประมาณ {days_left_60} วัน จนถึงอายุ 60 ปี")
    sleep_60, work_60, personal_60 = calculate_time_usage(days_left_60)
    print(f"  - เวลานอน: {sleep_60} ชั่วโมง")
    print(f"  - เวลาทำงาน: {work_60} ชั่วโมง")
    print(f"  - เวลาส่วนตัว: {personal_60} ชั่วโมง")
else:
    print("คุณมีอายุ 60 ปีแล้ว หรือมากกว่านั้น")

# คำนวณวันที่เหลือถึงอายุ 75 ปี
days_left_75 = calculate_days_left(birth_day, birth_month, birth_year, 75)
if days_left_75 > 0:
    print(f"คุณเหลือเวลาอีกประมาณ {days_left_75} วัน จนถึงอายุ 75 ปี")
    sleep_75, work_75, personal_75 = calculate_time_usage(days_left_75)
    print(f"  - เวลานอน: {sleep_75} ชั่วโมง")
    print(f"  - เวลาทำงาน: {work_75} ชั่วโมง")
    print(f"  - เวลาส่วนตัว: {personal_75} ชั่วโมง")
else:
    print("คุณมีอายุ 75 ปีแล้ว หรือมากกว่านั้น")

# คำนวณวันที่เหลือถึงอายุ 100 ปี
days_left_100 = calculate_days_left(birth_day, birth_month, birth_year, 100)
if days_left_100 > 0:
    print(f"คุณเหลือเวลาอีกประมาณ {days_left_100} วัน จนถึงอายุ 100 ปี")
    sleep_100, work_100, personal_100 = calculate_time_usage(days_left_100)
    print(f"  - เวลานอน: {sleep_100} ชั่วโมง")
    print(f"  - เวลาทำงาน: {work_100} ชั่วโมง")
    print(f"  - เวลาส่วนตัว: {personal_100} ชั่วโมง")
else:
    print("คุณมีอายุ 100 ปีแล้ว หรือมากกว่านั้น")

# คำนวณเวลาทั้งหมดตั้งแต่เกิด
age_now = date.today().year - birth_year - ((date.today().month, date.today().day) < (birth_month, birth_day))
days_lived = (date.today() - date(birth_year, birth_month, birth_day)).days
hours_lived_sleep = days_lived * 8
hours_lived_work = days_lived * 8
hours_lived_personal = days_lived * 8

print(f"คุณมีอายุ {age_now} ปีแล้ว")
print(f"คุณใช้เวลาไปแล้วทั้งหมด {days_lived} วัน")
print(f"  - เวลานอน: {hours_lived_sleep} ชั่วโมง")
print(f"  - เวลาทำงาน: {hours_lived_work} ชั่วโมง")
print(f"  - เวลาส่วนตัว: {hours_lived_personal} ชั่วโมง")

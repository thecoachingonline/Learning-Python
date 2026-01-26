from datetime import date

def calculate_days_left(birth_month, birth_year):
    """คำนวณจำนวนวันที่เหลืออยู่จนถึงอายุ 75 ปี"""

    today = date.today()
    birth_date = date(birth_year, birth_month, 1)

    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    target_year = birth_date.year + 75
    target_date = date(target_year, birth_month, 1)

    days_left = (target_date - today).days

    return days_left, age

def calculate_time_until_60(birth_month, birth_year):
    """คำนวณเวลาทำงาน, เวลานอน, และเวลาส่วนตัวจนถึงอายุ 60 ปี"""

    today = date.today()
    birth_date = date(birth_year, birth_month, 1)

    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    target_year_60 = birth_date.year + 60
    target_date_60 = date(target_year_60, birth_month, 1)

    days_until_60 = (target_date_60 - today).days

    if days_until_60 > 0:
        working_hours = days_until_60 * 8
        sleeping_hours = days_until_60 * 8
        personal_hours = days_until_60 * 8
        return days_until_60, working_hours, sleeping_hours, personal_hours
    else:
        return 0, 0, 0, 0

# รับข้อมูลเดือนและปีเกิดจากผู้ใช้
birth_month = int(input("กรุณาใส่เดือนเกิด (1-12): "))
birth_year = int(input("กรุณาใส่ปีเกิด (พ.ศ.): "))

# แปลงปี พ.ศ. เป็น ค.ศ.
birth_year -= 543

# คำนวณและแสดงผลลัพธ์
days_left, current_age = calculate_days_left(birth_month, birth_year)
days_until_60, working_hours, sleeping_hours, personal_hours = calculate_time_until_60(birth_month, birth_year)

if days_left > 0:
    print(f"คุณมีอายุ {current_age} ปี")
    print(f"คุณเหลือเวลาอีกประมาณ {days_left} วัน จนถึงอายุ 75 ปี")
    if days_until_60 > 0:
        print(f"จนถึงอายุ 60 ปี คุณจะ:")
        print(f"  มีเวลาทำงานประมาณ {working_hours} ชั่วโมง")
        print(f"  มีเวลานอนประมาณ {sleeping_hours} ชั่วโมง")
        print(f"  มีเวลาส่วนตัวประมาณ {personal_hours} ชั่วโมง")
    else:
        print("คุณมีอายุ 60 ปีแล้ว หรือมากกว่านั้น")
else:
    print("คุณมีอายุ 75 ปีแล้ว หรือมากกว่านั้น")



#๒๖J
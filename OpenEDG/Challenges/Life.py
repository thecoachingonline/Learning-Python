from datetime import date

def calculate_days_left(birth_month, birth_year):
    """คำนวณจำนวนวันที่เหลืออยู่จนถึงอายุ 75 ปี"""

    today = date.today()
    birth_date = date(birth_year, birth_month, 1)  # วันที่ 1 ของเดือนเกิด

    # คำนวณอายุของผู้ใช้ในปัจจุบัน
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    # คำนวณปีที่ผู้ใช้จะมีอายุ 75 ปี
    target_year = birth_date.year + 75

    # สร้างวันที่เป้าหมาย (วันเกิดในปีที่อายุ 75 ปี)
    target_date = date(target_year, birth_month, 1)

    # คำนวณจำนวนวันที่เหลืออยู่
    days_left = (target_date - today).days

    return days_left

# รับข้อมูลเดือนและปีเกิดจากผู้ใช้
birth_month = int(input("กรุณาใส่เดือนเกิด (1-12): "))
birth_year = int(input("กรุณาใส่ปีเกิด (พ.ศ.): "))

# แปลงปี พ.ศ. เป็น ค.ศ.
birth_year -= 543

# คำนวณและแสดงผลลัพธ์
days_left = calculate_days_left(birth_month, birth_year)

if days_left > 0:
    print(f"คุณเหลือเวลาอีกประมาณ {days_left} วัน จนถึงอายุ 75 ปี")
else:
    print("คุณมีอายุ 75 ปีแล้ว หรือมากกว่านั้น")


#๑๔
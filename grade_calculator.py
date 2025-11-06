# grade_calculator.py

# โปรแกรมคำนวณเกรดจากคะแนนของผู้ใช้

# รับข้อมูลจากผู้ใช้ (input() จะได้ข้อมูลเป็น 'string')
name = input("กรุณากรอกชื่อนักเรียน: ")
score = float(input("กรุณากรอกคะแนน (0-100): "))

# เงื่อนไขการให้เกรด (if / elif / else)
if score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
elif score >= 50:
    grade = "D"
else:
    grade = "F"

# แสดงผลลัพธ์
print(f"ชื่อ: {name}")
print(f"คะแนนที่ได้: {score}")
print(f"เกรดของคุณคือ: {grade}")

# Functions

# 1ฟังก์ชันทักทาย
def say_hello():
    print("สวัสดี ")

say_hello()
print("----------")

# 2ฟังก์ชันที่รับค่า
def greet(name):
    print("ยินดีที่ได้รู้จัก,", name, "")

greet("Fern")
print("----------")

# 3ฟังก์ชันที่มีการ return
def add(a, b):
    return a + b

sum_result = add(10, 5)
print("ผลรวมของ 10 + 5 =", sum_result)
print("----------")

# 4ฟังก์ชันตัดเกรด 
def get_grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

print("เกรดของคุณคือ:", get_grade(85))
print("เกรดของคุณคือ:", get_grade(49))
print("----------")

# 5ฟังก์ชันท้าทาย: แปลงองศา
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print("30°C =", celsius_to_fahrenheit(30), "°F")

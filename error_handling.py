#Error Handling

def divide(a, b):
    try:
        result = a / b
        print(f"ผลลัพธ์ของ {a} ÷ {b} = {result}")
    except ZeroDivisionError:
        print(" ห้ามหารด้วยศูนย์!")
    except TypeError:
        print("ใส่เฉพาะตัวเลขเท่านั้น!")
    finally:
        print("จบการคำนวณ \n")

# ทดสอบ
divide(10, 2)
divide(5, 0)
divide("10", 2)

# อ่านไฟล์อย่างปลอดภัย
try:
    with open("users.txt", "r", encoding="utf-8") as f:
        data = f.read()
        print("ข้อมูลในไฟล์:")
        print(data)
except FileNotFoundError:
    print(" ไม่พบไฟล์ users.txt")

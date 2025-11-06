import os
import shutil

# แสดง path ปัจจุบัน
print(" โฟลเดอร์ปัจจุบัน:", os.getcwd())

# สร้างโฟลเดอร์ใหม่
os.makedirs("test_folder", exist_ok=True)
print(" สร้างโฟลเดอร์ test_folder แล้ว")

# สร้างไฟล์ตัวอย่าง
with open("test_folder/example.txt", "w", encoding="utf-8") as f:
    f.write("Hello Fern! ")

# ตรวจสอบไฟล์ทั้งหมดในโฟลเดอร์
files = os.listdir("test_folder")
print(" ไฟล์ในโฟลเดอร์:", files)



#ย้ายไฟล์ (Move / Copy)

# ย้ายไฟล์
os.makedirs("backup", exist_ok=True)
shutil.move("test_folder/example.txt", "backup/example.txt")
print("ย้าย example.txt ไปที่ backup แล้ว")

# คัดลอกไฟล์กลับมา
shutil.copy("backup/example.txt", "test_folder/example_copy.txt")
print(" คัดลอกกลับมาที่ test_folder แล้ว")


#ลบไฟล์และโฟลเดอร์

os.remove("test_folder/example_copy.txt")
print(" ลบไฟล์ตัวอย่างแล้ว")

# ลบทั้งโฟลเดอร์ (และไฟล์ภายใน)
shutil.rmtree("test_folder")
print(" ลบโฟลเดอร์ test_folder แล้ว")


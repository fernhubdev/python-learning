# File Handling

# --- เขียนข้อมูลลงไฟล์ ---
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("บันทึกการเรียน Python\n")
    file.write("การจัดการไฟล์\n")
    file.write("เขียนและอ่านไฟล์สำเร็จแล้ว!\n")

print(" สร้างไฟล์ notes.txt สำเร็จ")

print("----------")

# --- อ่านข้อมูลจากไฟล์ ---
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()

print("เนื้อหาในไฟล์คือ:")
print(content)

print("----------")

# --- เพิ่มข้อความต่อท้าย ---
with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("เพิ่มบันทึกใหม่ต่อท้ายไฟล์!\n")

print(" เพิ่มข้อความใหม่เรียบร้อยแล้ว")

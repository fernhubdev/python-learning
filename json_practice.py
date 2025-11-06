import json

# สร้างข้อมูลเป็น dictionary
user_data = {
    "name": "Fern",
    "age": 23,
    "skills": ["Python", "Git", "Data"],
    "active": True
}

# บันทึกข้อมูลลงไฟล์ JSON
with open("user_data.json", "w", encoding="utf-8") as file:
    json.dump(user_data, file, indent=4)
print(" บันทึกข้อมูลเรียบร้อยแล้ว!")

# โหลดข้อมูลกลับมาอ่าน
with open("user_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    print("\n ข้อมูลที่โหลดได้:")
    print(data)

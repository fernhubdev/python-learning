# List and Dictionary

# --- List Section ---
pets = ["หมา", "แมว", "นก"]
print("สัตว์เลี้ยงทั้งหมด:", pets)

# เพิ่มตัวใหม่
pets.append("กระต่าย")
print("หลังเพิ่ม:", pets)

# ลบออก 1 ตัว
pets.remove("แมว")
print("หลังลบ:", pets)

# วนแสดงผลทั้งหมด
for pet in pets:
    print("ฉันรัก", pet)

print("----------")

# --- Dictionary Section ---
pet_info = {
    "name": "Luna",
    "type": "Dog",
    "age": 3
}

print("ข้อมูลสัตว์เลี้ยง:", pet_info)

# เพิ่มข้อมูลใหม่
pet_info["color"] = "white"

# แก้ไขอายุ
pet_info["age"] = 4

# แสดงผลทั้งหมด
for key, value in pet_info.items():
    print(key, ":", value)

print("----------")

# ท้าทาย: เก็บสัตว์หลายตัวใน list ของ dictionary
all_pets = [
    {"name": "Luna", "type": "Dog"},
    {"name": "Milo", "type": "Cat"},
    {"name": "Coco", "type": "Bird"}
]

for pet in all_pets:
    print(pet["name"], "เป็น", pet["type"])

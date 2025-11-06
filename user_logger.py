# Mini Project – โปรแกรมบันทึกข้อมูลผู้ใช้

users = []  # list เก็บข้อมูลผู้ใช้

print("=== โปรแกรมบันทึกข้อมูลผู้ใช้ ===")

while True:
    name = input("กรอกชื่อ (หรือพิมพ์ 'exit' เพื่อจบ): ")
    if name.lower() == "exit":
        break

    age = input("กรอกอายุ: ")
    email = input("กรอกอีเมล: ")

    # สร้าง dictionary เก็บข้อมูล 1 คน
    user = {"name": name, "age": age, "email": email}
    users.append(user)
    print(" บันทึกข้อมูลของ", name, "เรียบร้อยแล้ว!\n")

# --- บันทึกข้อมูลลงไฟล์ ---
with open("users.txt", "w", encoding="utf-8") as file:
    for user in users:
        file.write(f"{user['name']},{user['age']},{user['email']}\n")

print(" บันทึกข้อมูลทั้งหมดลงในไฟล์ users.txt แล้ว!")

# --- อ่านข้อมูลกลับมาแสดงผล ---
print("\n=== ข้อมูลทั้งหมดในไฟล์ ===")
with open("users.txt", "r", encoding="utf-8") as file:
    for line in file:
        name, age, email = line.strip().split(",")
        print(f"ชื่อ: {name} | อายุ: {age} | อีเมล: {email}")

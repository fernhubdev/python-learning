import sqlite3

# สร้างหรือเชื่อมต่อกับฐานข้อมูล (ไฟล์ .db)
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# สร้างตาราง
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
)
""")

# เพิ่มข้อมูล
cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", 
               ("Fern", 23, "fern@example.com"))

# บันทึกการเปลี่ยนแปลง
conn.commit()

# ดึงข้อมูลทั้งหมด
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print("\n รายชื่อผู้ใช้:")
for row in rows:
    print(row)

# ปิดการเชื่อมต่อ
conn.close()

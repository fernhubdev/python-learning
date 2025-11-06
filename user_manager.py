import sqlite3

def create_table():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        email TEXT UNIQUE
    )
    """)
    conn.commit()
    conn.close()

def add_user(name, age, email):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", (name, age, email))
    conn.commit()
    conn.close()
    print(f" เพิ่ม {name} เรียบร้อยแล้ว!")

def view_users():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def delete_user(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    print(f" ลบผู้ใช้ ID {user_id} เรียบร้อย")

# --- เริ่มโปรแกรม ---
create_table()

while True:
    print("\n--- ระบบจัดการผู้ใช้ ---")
    print("1. เพิ่มผู้ใช้")
    print("2. ดูผู้ใช้ทั้งหมด")
    print("3. ลบผู้ใช้")
    print("4. ออกจากโปรแกรม")

    choice = input("เลือกเมนู: ")

    if choice == "1":
        name = input("ชื่อ: ")
        age = int(input("อายุ: "))
        email = input("อีเมล: ")
        add_user(name, age, email)
    elif choice == "2":
        view_users()
    elif choice == "3":
        user_id = int(input("กรอก ID ที่ต้องการลบ: "))
        delete_user(user_id)
    elif choice == "4":
        break
    else:
        print(" เลือกเมนูไม่ถูกต้อง!")

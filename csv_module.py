#CSV and Modules

import csv

# สร้างข้อมูลตัวอย่าง
users = [
    ["ชื่อ", "อายุ", "อีเมล"],
    ["Fern", 23, "fern@example.com"],
    ["First", 24, "first@example.com"],
    ["Mint", 21, "mint@example.com"]
]

# เขียนข้อมูลลงไฟล์ CSV
with open("users.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(users)

print(" เขียนไฟล์ users.csv เสร็จแล้ว!")

from csv_tools import save_to_csv, read_csv

data = [
    ["ชื่อ", "อายุ"],
    ["Fern", 23],
    ["First", 24]
]

save_to_csv("data.csv", data)

print("ข้อมูลที่อ่านกลับมา:")
for row in read_csv("data.csv"):
    print(row)

# Average Calculator
# โปรแกรมคำนวณค่าเฉลี่ยคะแนนหลายวิชา

print("=== โปรแกรมคำนวณค่าเฉลี่ยคะแนน ===")

# ให้ผู้ใช้กรอกจำนวนวิชา
num_subjects = int(input("กรอกจำนวนวิชา: "))

scores = []  # สร้างลิสต์เก็บคะแนน

# วนรับคะแนนแต่ละวิชา
for i in range(num_subjects):
    score = float(input(f"กรอกคะแนนวิชา {i+1}: "))
    scores.append(score)

# คำนวณค่าเฉลี่ย
average = sum(scores) / len(scores)

print("---------------------------")
print(f"คะแนนทั้งหมด: {scores}")
print(f"ค่าเฉลี่ยคะแนนของคุณคือ: {average:.2f}")

# เพิ่มฟีเจอร์ bonus
if average >= 80:
    print("คุณได้เกรด A")
elif average >= 70:
    print("คุณได้เกรด B")
elif average >= 60:
    print("คุณได้เกรด C")
else:
    print("คุณได้เกรด D หรือ F")

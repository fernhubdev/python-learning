# Loops

# 1 พิมพ์เลข 1 ถึง 10 ด้วย for loop
for i in range(1, 11):
    print(i)

print("----------")

# 2 แสดงผลรวมของเลข 1 ถึง 100
total = 0
for i in range(1, 101):
    total += i
print("ผลรวมของเลข 1 ถึง 100 คือ:", total)

print("----------")

# 3 while loop: นับถอยหลังจาก 5 ถึง 1
count = 5
while count > 0:
    print(count)
    count -= 1
print("เริ่มได้เลย! ")

print("----------")

# 4 ลองใช้ loop กับ list
pets = ["หมา", "แมว", "นก"]
for animal in pets:
    print("ฉันชอบ", animal)

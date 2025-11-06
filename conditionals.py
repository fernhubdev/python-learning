# Conditionals

# โปรแกรมทายอายุ
age = int(input("กรุณาใส่อายุของคุณ: "))

if age < 13:
    print("คุณยังเป็นเด็กอยู่เลย ")
elif age < 20:
    print("คุณเป็นวัยรุ่น ")
elif age < 60:
    print("คุณเป็นผู้ใหญ่ ")
else:
    print("คุณเป็นผู้สูงอายุ ")
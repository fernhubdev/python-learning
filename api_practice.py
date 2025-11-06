import requests
import json

# ตัวอย่าง: ดึงข้อมูลสุ่มหมา (Random Dog API)
url = "https://dog.ceo/api/breeds/image/random"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(" ดึงข้อมูลสำเร็จ!")
    print("รูปหมาแบบสุ่มคือ:", data["message"])

    # บันทึกข้อมูลลงไฟล์
    with open("dog_api.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    print("\n บันทึกข้อมูลลงไฟล์เรียบร้อยแล้ว!")
else:
    print(" ไม่สามารถดึงข้อมูลได้ (status:", response.status_code, ")")

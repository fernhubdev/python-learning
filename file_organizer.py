import os
import shutil

def organize_files(folder_path):
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            ext = filename.split(".")[-1].lower()
            target_folder = os.path.join(folder_path, ext)

            # สร้างโฟลเดอร์ตามนามสกุล
            os.makedirs(target_folder, exist_ok=True)

            # ย้ายไฟล์เข้าโฟลเดอร์
            shutil.move(
                os.path.join(folder_path, filename),
                os.path.join(target_folder, filename)
            )
            print(f" ย้าย {filename} ไปที่ {ext}/")

folder = input(" ป้อน path ของโฟลเดอร์ที่ต้องการจัดระเบียบ: ")
organize_files(folder)
print(" จัดระเบียบไฟล์เรียบร้อยแล้ว!")

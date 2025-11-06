import logging
from datetime import datetime

# ตั้งค่าการบันทึก log ให้รองรับภาษาไทย
logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S',
    encoding='utf-8'  
)

logging.info("เริ่มต้นโปรแกรม")
logging.debug("โหลดข้อมูลผู้ใช้...")
logging.warning("ข้อมูลบางส่วนอาจไม่ครบ")
logging.error("เกิดข้อผิดพลาดในการเชื่อมต่อฐานข้อมูล")
logging.critical("ระบบล่ม! ต้องรีบตรวจสอบ")

print(" โปรแกรมทำงานเสร็จแล้ว — ไปดูไฟล์ app.log ได้เลย!")


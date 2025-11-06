# Date & Time

import datetime

# แสดงวันและเวลาปัจจุบัน
now = datetime.datetime.now()
print(" เวลาปัจจุบันคือ:", now)

# แสดงเฉพาะวันที่หรือเวลา
print(" วันที่:", now.date())
print(" เวลา:", now.time())


print("ปี:", now.year)
print("เดือน:", now.month)
print("วัน:", now.day)

#การคำนวณระยะห่างระหว่างวัน

from datetime import date

birthday = date(2001, 7, 21)
today = date.today()

age_days = (today - birthday).days
age_years = age_days // 365

print(f" Fern อายุประมาณ {age_years} ปี ({age_days} วัน)")



#การเพิ่มหรือลดเวลา (timedelta)

from datetime import timedelta

tomorrow = now + timedelta(days=1)
print("พรุ่งนี้คือ:", tomorrow.strftime("%d/%m/%Y"))

last_week = now - timedelta(days=7)
print("เมื่อสัปดาห์ก่อนคือ:", last_week.strftime("%d/%m/%Y"))

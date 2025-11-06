import datetime

def log_time(action):
    now = datetime.datetime.now()
    formatted_time = now.strftime("%d/%m/%Y %H:%M:%S")
    
    with open("work_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{action} เวลา {formatted_time}\n")
    
    print(f" บันทึก {action} แล้ว ({formatted_time})")

# ใช้งาน
log_time("เข้างาน")
log_time("ออกงาน")
